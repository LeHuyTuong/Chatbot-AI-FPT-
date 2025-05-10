  GNU nano 6.2                                                                                           app.py
import gradio as gr
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load vector DB
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory="./vector_db", embedding_function=embedding)

# Query function
def ask_bot(query):
    docs = db.similarity_search(query, k=5)
    return "\n\n".join([f"📌 {doc.page_content}" for doc in docs])

# Gradio UI
iface = gr.Interface(
    fn=ask_bot,
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything about FPT..."),
    outputs="text",
    title="FPT RAG Chatbot",
)

iface.launch(server_name="0.0.0.0", server_port=7860)














