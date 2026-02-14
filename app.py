import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

from retriever import get_retriever
from prompt import build_prompt,SYSTEM_PROMPT   # use system directly

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = "rag-secret-key"

# Init retriever once
retriever = get_retriever()

# Init LLM
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

    FITNESS_WORDS = [
    # Body & measurements
    "weight","height","bmi","body","fat","fat%", "muscle","mass","lean",
    "waist","hip","chest","shoulder","arm","leg","thigh","calf",

    # Training & exercise
    "gym","workout","exercise","training","cardio","strength","lifting",
    "run","running","jog","walk","walking","cycling","swimming",
    "pushup","pullup","squat","deadlift","bench","plank","stretch",

    # Muscles
    "biceps","triceps","chest","back","shoulders","abs","core","quads",
    "hamstring","glutes","lats","forearms","traps",

    # Nutrition
    "diet","food","meal","calories","kcal","protein","carbs","fat",
    "fiber","vitamin","minerals","hydration","water","milk","eggs",
    "rice","roti","dal","chicken","paneer","banana","oats",

    # Goals
    "fat loss","weight loss","muscle gain","bulking","cutting","shredded",
    "leaning","toned","fit","fitness",

    # Recovery & health habits
    "sleep","rest","recovery","steps","heart rate","metabolism","energy",

    # Supplements (common)
    "whey","protein powder","creatine","multivitamin","omega","bcaa"
]
    
    if not any(word in user_msg.lower() for word in FITNESS_WORDS):

        return jsonify({
            "response": "• Stay focused. Distractions don’t build strong bodies 🔥\n"
                        "• Train harder. Eat clean. Level up 🏋️\n"
                        "• Back to work. Back to progress 💧\n(M)"
        })



    # Initialize memory
    if "history" not in session:
        session["history"] = []

    # Retrieve docs
    docs = retriever.invoke(user_msg)
    print("FOUND: ", len(docs))

    # Build context
    context = "\n\n".join(d.page_content for d in docs)

    source_snippets = "\n\n".join(
    "📄 " + " ".join(doc.page_content.strip().split()[:80]) + "..."
    for doc in docs
)




    # Memory
    memory_text = ""
    for u, a in session["history"][-3:]:
        memory_text += f"User: {u}\nAssistant: {a}\n"

    # Build prompt (ALWAYS runs)
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"""
    PREVIOUS CONVERSATION:
    {memory_text}

    CONTEXT:
    {context}

    QUESTION:
    {user_msg}

    ANSWER IN POINTS:
    """)
    ]

    response = llm.invoke(messages).content


    # Save memory
    session["history"].append((user_msg, response))
    session.modified = True

    source_snippets_html = source_snippets.replace("\n", "<br>")
    final_answer = f"""
    <div style="white-space: pre-line;">
    {response}
    </div>

    <hr>

    <button class="ref-toggle" onclick="toggleRefs()">📚 Show knowledge base references</button>

    <div id="rag-refs" class="rag-ref hidden">
    <b>References from knowledge base</b><br><br>
    {source_snippets_html}
    </div>

    <script>
    function toggleRefs() {{
        const box = document.getElementById("rag-refs");
        box.classList.toggle("hidden");
    }}
    </script>
    """

    return jsonify({"response": final_answer})


@app.route("/reset", methods=["POST"])
def reset():
    session.pop("history", None)
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    app.run(debug=False, port=8080)
