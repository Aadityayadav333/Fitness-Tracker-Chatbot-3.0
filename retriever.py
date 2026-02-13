# retriever.py

import os
from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv
load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAISS_PATH = os.path.join(BASE_DIR, "faiss_index")

def get_retriever():
    # Cohere cloud embeddings (no local models)
    embeddings = CohereEmbeddings(
        model="embed-english-v3.0"
    )

    vectorstore = FAISS.load_local(
        FAISS_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )
