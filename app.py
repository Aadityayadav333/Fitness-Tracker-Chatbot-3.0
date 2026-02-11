import os
from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from retriever import get_retriever
from prompt import build_prompt

load_dotenv()

app = Flask(__name__)
app.secret_key = "rag-secret-key"  # for session memory

# Init once
retriever = get_retriever()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.2
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]

    # init memory
    if "history" not in session:
        session["history"] = []

    # retrieve RAG context
    docs = retriever.invoke(user_msg)
    context = "\n\n".join(d.page_content for d in docs)

    # include short memory (last 3 turns)
    memory_text = ""
    for u, a in session["history"][-3:]:
        memory_text += f"User: {u}\nAssistant: {a}\n"

    full_prompt = f"""
Previous conversation:
{memory_text}

{build_prompt(context, user_msg)}
"""

    response = llm.invoke(full_prompt).content

    # save memory
    session["history"].append((user_msg, response))
    session.modified = True

    return jsonify({"response": response})


@app.route("/reset", methods=["POST"])
def reset():
    session.pop("history", None)
    return jsonify({"status": "cleared"})



if __name__ == "__main__":
    app.run(debug=True, port=8080)


