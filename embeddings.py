import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env automatically

COHERE_API_KEY = os.environ["COHERE_API_KEY"]

# Paths
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

    # 2. Chunk text for RAG
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80,
        separators=["\n\n", "\n", ".", " "]
    )
    docs = splitter.create_documents([text])

    # 3. Cohere cloud embeddings (lightweight)
    embeddings = CohereEmbeddings(
        model="embed-english-v3.0",   # best current Cohere embedding model
        cohere_api_key= os.environ["COHERE_API_KEY"]
    )

    # 4. Build FAISS vector DB
    vectorstore = FAISS.from_documents(docs, embeddings)

    # 5. Save locally (or inside container)
    vectorstore.save_local(DB_PATH)

    print(f"FAISS index created with {len(docs)} chunks at {DB_PATH}")

if __name__ == "__main__":
    create_embeddings()
