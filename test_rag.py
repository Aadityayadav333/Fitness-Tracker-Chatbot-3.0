# backend/rag/test_rag.py

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from backend.rag.retriever import get_retriever
from backend.rag.prompt import build_prompt

load_dotenv()

def run_rag_query(question):
    retriever = get_retriever()

    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join([doc.page_content for doc in docs])

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant",
        temperature=0.2
    )

    prompt = build_prompt(context, question)

    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    query = "What should i eat for breakfast muscle building diet"
    answer = run_rag_query(query)

    print("\n🔍 QUERY:", query)
    print("-" * 50)
    print(answer)
