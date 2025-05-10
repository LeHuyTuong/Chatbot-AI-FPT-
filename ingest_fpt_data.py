import json
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def clean_metadata(metadata):
    return {k: v for k, v in metadata.items() if isinstance(v, (str, int, float, bool))}

with open("fpt_chunks_enriched.jsonl", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
    data = [json.loads(line) for line in lines]

documents = [
    Document(page_content=item["text"], metadata=clean_metadata(item["metadata"]))
    for item in data
]

db = Chroma.from_documents(documents, embedding, persist_directory="./vector_db")
db.persist()
print("✅ Vector DB đã tạo thành công không lỗi metadata.")

