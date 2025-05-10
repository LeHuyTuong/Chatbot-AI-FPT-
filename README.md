
# FPT RAG Local Pipeline (LangChain + Chroma + HuggingFace)

## 📅 Date: 2025-05-10

## 🚀 Objective
Build a Retrieval-Augmented Generation (RAG) pipeline using FPT University 2025 admission data — completely **local**, with no OpenAI dependency.

## OUTPUT
![image](https://github.com/user-attachments/assets/f6fad3f7-cd68-482a-af7f-86cb1d88a045)


---

## ✅ Completed Steps

### 1. Document Chunking
- 📄 Source: `THÔNG TIN ĐẠI HỌC FPT 2025.docx`
- ✅ Extracted and split into JSONL chunks:
  - `text`: logical content segment
  - `metadata`: includes `campus`, `major`, `sub_major`, `scholarship_type`, etc.
- 🔧 Saved as: `fpt_chunks_enriched.jsonl`

---

### 2. Environment Setup
- Used **Linux VPS**
- Installed Python, virtualenv, and required packages:
```bash
python3 -m venv venv
source venv/bin/activate
pip install langchain langchain-community chromadb sentence-transformers
```

---

### 3. Embedding & Vector Storage
- ✅ Bypassed OpenAI due to quota limits
- 📦 Used HuggingFace model: `all-MiniLM-L6-v2`
- 🧠 Persisted into Chroma vector store (`./vector_db`)
- Run via `ingest_fpt_data.py`

---

### 4. RAG-style Query Interface
- Built `query_rag.py` for terminal-based questions
- Returns top 5 most similar text chunks (`k=5`)
- ✅ Merged text output for readability
- ✅ Displayed associated metadata for each chunk

---

## 📂 Project Structure

```
fpt_rag/
├── fpt_chunks_enriched.jsonl
├── ingest_fpt_data.py
├── query_rag.py
├── vector_db/            # auto-generated vector storage
└── venv/                 # Python virtual environment
```

---

## ✍️ Suggestions for Improvement
- Add a local LLM for summarization or response generation
- Build a web interface using FastAPI or Streamlit
- Replace Chroma with FAISS or Weaviate for scalability

---

## 👨‍💻 Credits
- Project built by: **Le Huy Tuong**
- Technical guidance: **ChatGPT (LangChain Expert Mode)**
