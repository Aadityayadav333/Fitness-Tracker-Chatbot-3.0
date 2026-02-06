import os
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate

# Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "faiss_index")

def get_diet_response(user_data, user_query):
    # 1. Initialize the same embeddings used in creation
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # 2. Load the Vector Database
    # Note: allow_dangerous_deserialization is required for loading local pickle files
    vectorstore = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)

    # 3. Setup Groq (Get your free key from console.groq.com)
    llm = ChatGroq(
        temperature=0.2, 
        groq_api_key="YOUR_GROQ_API_KEY", 
        model_name="llama3-8b-8192" 
    )

    # 4. Custom Prompt to include BMI/User context
    template = """
    You are a professional Diet & Health Assistant. 
    User Profile: {user_context}
    
    Use the following nutrition knowledge to answer the user's question.
    Context: {context}
    
    User Question: {question}
    
    Answer:"""
    
    prompt = PromptTemplate(
        template=template, 
        input_variables=["user_context", "context", "question"]
    )

    # 5. Create the Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": prompt}
    )

    # Combine user data (BMI, age, etc.) into a string for the LLM
    user_context_str = f"BMI: {user_data['bmi']}, Goal: {user_data['goal']}, Weight: {user_data['weight']}kg"
    
    response = qa_chain.invoke({"query": user_query, "user_context": user_context_str})
    return response["result"]