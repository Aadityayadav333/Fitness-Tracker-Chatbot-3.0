import os
from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

def load_knowledge_base():
    # Example: load your text files / data here
    docs = []

    with open("documents/nutrition_knowledge.txt", "r", encoding="utf-8") as f:
        text = f.read()
        chunks = text.split("\n\n")  # simple chunking

        for chunk in chunks:
            docs.append(Document(page_content=chunk))

    return docs


def get_retriever():
    embeddings = CohereEmbeddings(model="embed-english-v3.0")

    documents = load_knowledge_base()

    vectorstore = FAISS.from_documents(
        documents,
        embeddings
    )

    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )
