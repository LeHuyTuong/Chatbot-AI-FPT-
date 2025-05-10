# 🧠 FPT University RAG Chatbot (Local LangChain + Chroma + HuggingFace)

> A fully local Retrieval-Augmented Generation (RAG) pipeline built with 100% open-source tools — no OpenAI key required.

📅 **Date**: May 10, 2025  
🛠 **Maintainer**: [Le Huy Tuong](https://github.com/LeHuyTuong)  
🌐 **Demo**: [Docker Hub](https://hub.docker.com/r/lehuytuong/fpt-rag-app)

---

## 🚀 Project Objective

Build a question-answering chatbot that uses **FPT University 2025 admission data** via semantic search on vector embeddings. Fully offline and dockerized.

---

## ✅ Features

- 📄 Document parsing and metadata-enriched chunking
- 🧠 Embedding via HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)
- 🗃️ Vector store via `Chroma`
- 🖥️ Terminal + Web UI (Gradio)
- 🐳 Docker-ready deployment

---

## 📂 Folder Structure

```
fpt_rag/
├── app.py                   # Web UI via Gradio
├── fpt_chunks_enriched.jsonl  # Chunked document with metadata
├── ingest_fpt_data.py       # Load and embed documents
├── query_rag.py             # Terminal RAG query interface
├── requirements.txt
├── Dockerfile
└── vector_db/               # Auto-generated vector database
```

---

## 🛠️ Setup Guide

### 1. Install dependencies

```bash
sudo apt update
sudo apt install python3 python3-venv git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the ingestion pipeline

```bash
python3 ingest_fpt_data.py
```

This loads `fpt_chunks_enriched.jsonl` and stores embeddings in `vector_db/`.

### 3. Terminal Query Interface

```bash
python3 query_rag.py
```

You’ll get the top 5 most relevant chunks with metadata.

### 4. Web Chat UI (Gradio)

```bash
python3 app.py
```

Then open `http://localhost:7860` or expose via `ngrok` / public IP.

---

## 🐳 Docker Deployment

### 1. Build the Docker image

```bash
docker build -t fpt-rag-app .
```

### 2. Run the container

```bash
docker run --rm -it -p 7860:7860 fpt-rag-app
```

---

## 📸 Screenshot
![Screenshot 2025-05-10 154929](https://github.com/user-attachments/assets/3ed5f6bc-211e-4853-9570-217c546caa11)

```bash
pip install gradio
```
![Screenshot 2025-05-10 182136](https://github.com/user-attachments/assets/6d45daa1-f865-4d52-8576-eb209825c95c)



---


## 💡 Future Enhancements

- ✅ Integrate a local LLM for response generation
- 🌍 Add multi-language or campus filter in metadata
- 🔌 Serve as API with FastAPI backend
- ⚡ Replace Chroma with FAISS/Weaviate for scale

---

## 👨‍💻 Credits

- 👤 Developed by: [Le Huy Tuong](https://github.com/LeHuyTuong)
- 🤖 AI Assistance: ChatGPT (LangChain + RAG expert mode)

---

## 📝 License

MIT License – Free for use and distribution.
