from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory="./vector_db", embedding_function=embedding)

print("🟢 Gõ câu hỏi (hoặc 'exit' để thoát).")

while True:
    query = input("\n❓ Bạn hỏi gì: ").strip()
    if query.lower() in ["exit", "quit"]:
        print("👋 Tạm biệt!")
        break

    docs = db.similarity_search(query, k=10)  # lấy 5 đoạn liên quan nhất

    if not docs:
        print("⚠️ Không tìm thấy kết quả phù hợp.")
        continue

    print("\n📚 Nội dung tổng hợp:\n")
    combined_text = "\n---\n".join([doc.page_content for doc in docs])
    print(combined_text)

    print("\n📌 Metadata từng đoạn:")
    for i, doc in enumerate(docs, 1):
        print(f"{i}. {doc.metadata}")

