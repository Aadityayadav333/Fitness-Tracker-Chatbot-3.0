import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Use the modern integration package
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores import FAISS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_PATH = os.path.join(BASE_DIR, "documents", "nutrition_knowledge.txt")
DB_PATH = os.path.join(BASE_DIR, "faiss_index")

def create_embeddings():
    # 1. Load text
    if not os.path.exists(DOC_PATH):
        print(f"❌ Error: {DOC_PATH} not found!")
        return

    with open(DOC_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    # 2. Chunk text (RAG friendly)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80,
        separators=["\n\n", "\n", ".", " "]
    )
    docs = splitter.create_documents([text])

    # 3. Load embedding model (This uses your local CPU/GPU)
    # This specifically avoids the deprecated community class
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 4. Create FAISS index
    vectorstore = FAISS.from_documents(docs, embeddings)

    # 5. Save index
    vectorstore.save_local(DB_PATH)

    print(f"✅ FAISS index created with {len(docs)} chunks at {DB_PATH}")

if __name__ == "__main__":
    create_embeddings()