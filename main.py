import json
import os
import re
import sys
import typing as t
import warnings
import pathlib as pathlib

import boto3
import frontmatter
import typer
import weaviate
from botocore.client import ClientError, Config
from dotenv import load_dotenv
from pymongo import MongoClient
from rich import print as rprint
from rich.console import Console
from rich.json import JSON
from rich.panel import Panel
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
from weaviate.classes.config import Configure
from weaviate.util import generate_uuid5


load_dotenv()
console = Console()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("MONGO_DATABASE", "linguistics_kb")
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_BUCKET = os.getenv("MINIO_BUCKET")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

app = typer.Typer(help="📚 Linguistic Thesaurus CLI")


def get_mongo() -> MongoClient:
    return MongoClient(MONGO_URI)


def get_wv() -> weaviate.WeaviateClient:
    return weaviate.connect_to_local("localhost", 8080, 50051)


def get_s3() -> boto3.client:
    return boto3.client(
        "s3",
        endpoint_url=f"http://{MINIO_ENDPOINT}",
        aws_access_key_id=MINIO_ACCESS_KEY,
        aws_secret_access_key=MINIO_SECRET_KEY,
        config=Config(signature_version="s3v4"),
    )


def get_embedder() -> SentenceTransformer:
    return SentenceTransformer(EMBEDDING_MODEL)


def infer_tags(parts: tuple[str, ...]) -> list[str]:
    return [part.lower() for part in parts[:-1] if part.lower() != "assets" and part != "Thesaurus"]


def ensure_title(metadata: t.MutableMapping[str, t.Any], file_path: pathlib.Path) -> None:
    if not metadata.get("title"):
        metadata["title"] = (
            file_path.stem
            .replace("-", " ")
            .replace("_", " ")
            .title()
        )


def backfill_missing_tags() -> None:
    mongo_client = get_mongo()
    documents_collection = mongo_client[DATABASE_NAME].documents
    query = {"$or": [
        {"metadata": {"$exists": False}},
        {"metadata.tags": {"$exists": False}},
        {"metadata.tags": {"$size": 0}},
    ]}
    patched = 0
    for document in documents_collection.find(query, {"_id": 1}):
        tags = infer_tags(pathlib.Path(document["_id"]).parts)
        if tags:
            documents_collection.update_one({"_id": document["_id"]}, {"$set": {"metadata.tags": tags}})
            patched += 1
    mongo_client.close()
    if patched:
        rprint(f"[green]🔧 Back-filled tags for {patched} docs.[/green]")


@app.callback(invoke_without_command=True)
def _autoback(ctx: typer.Context) -> None:
    if ctx.invoked_subcommand is None:
        rprint(ctx.get_help())
        raise typer.Exit()
    backfill_missing_tags()


def _setup_weaviate_schema(weaviate_client: weaviate.WeaviateClient) -> None:
    collection_name = "LinguisticConcept"
    if not weaviate_client.collections.exists(collection_name):
        weaviate_client.collections.create(
            name=collection_name,
            description="Concept from thesaurus",
            vectorizer_config=Configure.Vectorizer.none(),
            properties=[weaviate.classes.config.Property("deleted", weaviate.classes.config.DataType.BOOL)],
        )
        rprint(f"[green]✅ Created collection '{collection_name}'.[/green]")
    else:
        rprint(f"[yellow]📋 Collection '{collection_name}' already exists.[/yellow]")


def _setup_minio_bucket(s3_client) -> None:
    try:
        s3_client.head_bucket(Bucket=MINIO_BUCKET)
        rprint(f"[yellow]📦 Bucket '{MINIO_BUCKET}' already exists.[/yellow]")
    except ClientError as error:
        if error.response["Error"]["Code"] == "404":
            s3_client.create_bucket(Bucket=MINIO_BUCKET)
            rprint(f"[green]✅ Created bucket '{MINIO_BUCKET}'.[/green]")
        else:
            raise error


@app.command()
def setup() -> None:
    console.print(Panel("[bold blue]Initial Setup[/bold blue]", expand=False))
    weaviate_client = get_wv()
    try:
        _setup_weaviate_schema(weaviate_client)
    finally:
        weaviate_client.close()
    _setup_minio_bucket(get_s3())


def _process_md(file_path: pathlib.Path, root_directory: pathlib.Path, s3_client) -> t.Mapping[str, t.Any]:
    post = frontmatter.load(file_path)
    metadata = post.metadata or {}
    ensure_title(metadata, file_path) 
    if not metadata.get("tags"):
        metadata["tags"] = infer_tags(file_path.relative_to(root_directory).parts)

    content = post.content
    for match in re.finditer(r"!\[(.*?)\]\((.*?)\)", content):
        _, image_location = match.groups()
        image_path = (file_path.parent / image_location).resolve()
        if image_path.exists():
            key = f"assets/{image_path.name}"
            s3_client.upload_file(str(image_path), MINIO_BUCKET, key)
            content = content.replace(image_location, f"http://{MINIO_ENDPOINT}/{MINIO_BUCKET}/{key}")

    return {
        "_id": str(file_path.relative_to(root_directory)),
        "metadata": metadata,
        "content": content,
        "raw_text": post.content,
        "image_urls": [],
    }


@app.command()
def ingest(directory: pathlib.Path = typer.Argument(..., help="Path to Thesaurus")) -> None:
    if not directory.is_dir():
        rprint(f"[red]❌ Directory not found: {directory}[/red]")
        raise typer.Exit(1)

    markdown_files = [file_path for file_path in directory.rglob("*.md") if "assets" not in file_path.parts]
    console.print(Panel(f"[bold green]Found {len(markdown_files)} markdown files[/bold green]", expand=False))

    mongo_client = get_mongo()
    weaviate_client = get_wv()
    s3_client = get_s3()
    embedder = get_embedder()
    documents_collection = mongo_client[DATABASE_NAME].documents
    weaviate_collection = weaviate_client.collections.get("LinguisticConcept")

    try:
        with weaviate_collection.batch.dynamic() as batch:
            for file_path in tqdm(markdown_files, desc="Processing"):
                document = _process_md(file_path, directory.parent, s3_client)
                documents_collection.replace_one({"_id": document["_id"]}, document, upsert=True)

                vector = embedder.encode(f"{document['metadata'].get('title','')}{document['raw_text']}").tolist()
                batch.add_object(
                    properties={
                        "title": document["metadata"].get("title", "No Title"),
                        "tags":  document["metadata"]["tags"],
                        "mongo_id": document["_id"],
                        "deleted": False,
                    },
                    vector=vector,
                    uuid=generate_uuid5(document["_id"]),
                )
        rprint("[green]✅ Ingestion finished successfully![/green]")
    finally:
        mongo_client.close()
        weaviate_client.close()


def _build_query(pairs: list[str]) -> t.Mapping[str, t.Any]:
    query = {}

    for pair in pairs:
        key, val = pair.split("=", 1)

        if key.endswith(".tags"):
            tags = [tag.strip() for tag in val.split(",")]
            pattern = "|".join(tags)

            query["$or"] = [
                {key: {"$elemMatch": {
                    "$regex": f"^({pattern})$",
                    "$options": "i"
                }}},
                {"_id": {"$regex": f"^Thesaurus/({pattern})/",
                         "$options": "i"}}
            ]

        elif key.endswith(".title"):
            query[key] = {"$regex": f"^{val}$", "$options": "i"}

        else:
            try:
                val = int(val)
            except ValueError:
                try:
                    val = float(val)
                except ValueError:
                    pass
            query[key] = val

    return query


@app.command()
def query(filters: list[str] = typer.Argument(..., help="key=value …"), limit: int = typer.Option(None, "--limit", "-l", help="Maximum number of results to display")) -> None:
    mongo_client = get_mongo()
    try:
        cursor = mongo_client[DATABASE_NAME].documents.find(_build_query(filters), {"content":0, "raw_text":0})
        results = [{
            "title": document["metadata"].get("title") or pathlib.Path(document["_id"]).stem.replace("_"," ").replace("-"," "),
            "path":  str(pathlib.Path(document["_id"]).relative_to("Thesaurus")),
            "tags":  document["metadata"].get("tags", [])
        } for document in cursor]
        
        total_found = len(results)
        if limit is not None and limit > 0:
            results = results[:limit]
        
        if results:
            console.print(JSON(json.dumps(results, indent=2)))
        else:
            rprint("[yellow]No documents found[/yellow]")
        
        if limit is not None and total_found > limit:
            rprint(f"\n[bold blue]Showing {len(results)} of {total_found} documents.[/bold blue]")
        else:
            rprint(f"\n[bold blue]Found {len(results)} documents.[/bold blue]")
    finally:
        mongo_client.close()


@app.command(name="semantic-search")
def semantic_search(text: str, limit: int = 5) -> None:
    weaviate_client = get_wv()
    embedder = get_embedder()
    try:
        vector = embedder.encode(text).tolist()
        search_results = weaviate_client.collections.get("LinguisticConcept").query.near_vector(
            near_vector=vector, limit=limit,
            return_metadata=["distance"],
            return_properties=["title","mongo_id"]
        )
        results = []
        for search_object in search_results.objects:
            title = search_object.properties.get("title") or pathlib.Path(search_object.properties["mongo_id"]).stem
            results.append({
                "title": title,
                "path": str(pathlib.Path(search_object.properties["mongo_id"]).relative_to("Thesaurus")),
                "distance": search_object.metadata.distance
            })
        
        if results:
            console.print(Panel(f"[bold green]Semantic Search Results for: '{text}'[/bold green]", expand=False))
            console.print(JSON(json.dumps(results, indent=2)))
        else:
            rprint("[yellow]No semantic matches found[/yellow]")
    finally:
        weaviate_client.close()


@app.command()
def update(filters: list[str], updates: list[str] = typer.Option(..., '--updates', help='Updates to apply')) -> None:
    mongo_client = get_mongo()
    try:
        filter_dict = {key: value for key, value in (pair.split("=",1) for pair in filters)}
        update_dict = {"$set": {key: value for key, value in (pair.split("=",1) for pair in updates)}}
        result = mongo_client[DATABASE_NAME].documents.update_many(filter_dict, update_dict)
        rprint(f"[green]✅ Matched {result.matched_count}, modified {result.modified_count} documents.[/green]")
    finally:
        mongo_client.close()


def _soft(mongo_id: str, deleted_flag: bool) -> None:
    weaviate_client = get_wv()
    try:
        collection = weaviate_client.collections.get("LinguisticConcept")
        objects = collection.query.fetch_objects(
            filters=weaviate.classes.query.Filter
                    .by_property("mongo_id").equal(mongo_id),
            limit=1
        ).objects
        if objects:
            collection.data.update(objects[0].uuid, {"deleted": deleted_flag})
            action = "Undeleted" if not deleted_flag else "Deleted"
            rprint(f"[green]✅ {action} '{mongo_id}'.[/green]")
        else:
            rprint(f"[red]❌ Document not found in vectors: '{mongo_id}'[/red]")
    finally:
        weaviate_client.close()


@app.command()
def delete(mongo_id: str) -> None:
    _soft(mongo_id, True)


@app.command()
def undelete(mongo_id: str) -> None:
    _soft(mongo_id, False)


if __name__ == "__main__":
    warnings.filterwarnings(
        "ignore",
        category=DeprecationWarning,
        module=r"botocore\.auth"
    )

    os.environ["PYTHONWARNINGS"] = "ignore::DeprecationWarning"
    os.environ['PYTHONWARNINGS'] = 'ignore'
    app()
