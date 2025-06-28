#!/bin/bash
set -Eeuo pipefail

CLI="python main.py"
THES_DIR="Thesaurus"
MONGO_ID_TO_DELETE="Thesaurus/Language/Inner-Structure/Phonology/Core/Phoneme.md"

source .env
export AWS_ACCESS_KEY_ID="${MINIO_ACCESS_KEY}"
export AWS_SECRET_ACCESS_KEY="${MINIO_SECRET_KEY}"

echo -e "\n🚀 1. Setting up Weaviate schema and MinIO bucket"
$CLI setup

echo -e "\n📚 2. Ingesting all *.md files from '${THES_DIR}'"
$CLI ingest "${THES_DIR}"

echo -e "\n🔍 3-A. Simple query - tag 'phonology' (limit 5)"
$CLI query metadata.tags=phonology --limit 5

echo -e "\n🔍 3-B. Simple query - exact title 'Attention Mechanisms'"
$CLI query 'metadata.title=Attention Mechanisms'

echo -e "\n🧩 3-C. Compound query - two tags (phonology + advanced) (limit 5)"
$CLI query metadata.tags=phonology metadata.tags=advanced --limit 5

echo -e "\n🧩 3-D. Compound query - two other tags (computational-linguistics + advanced) (limit 5)"
$CLI query metadata.tags=computational-linguistics metadata.tags=advanced --limit 5

echo -e "\n🤖 4. Semantic search: 'How does palatalization work?'"
$CLI semantic-search "How does palatalization work?" --limit 3

echo -e "\n🖼 5. MinIO: First 10 uploaded assets"
(
  set +o pipefail
  aws s3 ls "s3://${MINIO_BUCKET}/assets/" \
       --endpoint-url "http://${MINIO_ENDPOINT}" --recursive \
       2>/dev/null | head -n 10
)

echo -e "\n✏️ 6. Bulk update - adding metadata.level=advanced for documents with 'advanced' tag"
$CLI update metadata.tags=advanced --updates metadata.level=advanced

echo -e "\n🗑 7-A. Soft-delete a document"
$CLI delete "${MONGO_ID_TO_DELETE}"

echo -e "\n♻️ 7-B. Restore the same document"
$CLI undelete "${MONGO_ID_TO_DELETE}"

echo -e "\n✅ Demo completed - all CLI features demonstrated!"
