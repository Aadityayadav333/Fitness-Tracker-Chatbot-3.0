<div align="center">

# 🏋️ Fitness Tracker Chatbot 3.0

### *Your AI-Powered Personal Fitness Coach — Built with RAG + LLM*

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.2-black?style=for-the-badge&logo=flask&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.2.17-green?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.1-orange?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> *"Train hard. Eat clean. Ask smarter."*

</div>

---

## 📌 About

**Fitness Tracker Chatbot 3.0** is a domain-focused AI chatbot that answers all your fitness, nutrition, and body transformation queries — powered by **Retrieval-Augmented Generation (RAG)**. It combines a curated knowledge base of fitness documents with the speed of **LLaMA 3.1 via Groq** to deliver precise, grounded answers in real time.

Built entirely on Flask, LangChain, FAISS, and Cohere embeddings, the chatbot strictly stays on-topic — it will not discuss anything outside the fitness domain, ensuring every response is focused, relevant, and actionable.

## Demo at Work
https://fitness-tracker-chatbot-3-0.onrender.com/

---

## ✨ Features

- 🧠 **RAG Pipeline** — Retrieves relevant chunks from a curated fitness knowledge base before generating answers
- ⚡ **LLaMA 3.1 (8B Instant) via Groq** — Ultra-fast LLM inference with low latency
- 🔒 **Domain Filtering** — Intelligently filters out non-fitness questions and redirects users
- 💬 **Conversation Memory** — Maintains last 3 turns of context per session for coherent multi-turn chat
- 📚 **Source Transparency** — Toggle button reveals the exact knowledge base chunks used to generate the answer
- 🧬 **FAISS Vector Store** — Fast semantic similarity search over embedded fitness documents
- 🌐 **Flask Web Interface** — Clean, responsive chat UI served via Flask

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Web Framework | Flask 3.0.2 |
| LLM | LLaMA 3.1 8B Instant (via Groq) |
| LLM Orchestration | LangChain 0.2.17 |
| Embeddings | Cohere (via `langchain-cohere`) |
| Vector Store | FAISS CPU |
| Memory | Flask Session (sliding window, last 3 turns) |
| Environment | python-dotenv |
| Frontend | HTML + CSS (custom) |

---

## 📁 Project Structure

```
Fitness-Tracker-Chatbot-3.0/
│
├── app.py               # Flask app, routes, RAG chat logic
├── embeddings.py        # Document loading & FAISS index creation
├── retriever.py         # FAISS retriever initialization
├── prompt.py            # System prompt & prompt builder
├── test_rag.py          # RAG pipeline testing script
├── requirements.txt     # Python dependencies
├── .python-version      # Python version pin (3.10)
│
├── documents/           # 📄 Fitness knowledge base (PDFs/text files)
├── faiss_index/         # 🗂️ Pre-built FAISS vector index
├── templates/           # 🌐 HTML templates (index.html)
└── static/              # 🎨 CSS, JS, images
```

---

## 🔄 How It Works

```
User Question
     │
     ▼
Domain Filter ──── ❌ Non-fitness? → Motivational redirect
     │
     ✅ Fitness-related
     │
     ▼
FAISS Retriever → Fetch top-k relevant chunks from knowledge base
     │
     ▼
Prompt Builder → Combine [System Prompt + Memory + Context + Question]
     │
     ▼
Groq LLM (LLaMA 3.1) → Generate structured answer
     │
     ▼
Response + 📚 Source Toggle → Rendered in Chat UI
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Aadityayadav333/Fitness-Tracker-Chatbot-3.0.git
cd Fitness-Tracker-Chatbot-3.0
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
COHERE_API_KEY=your_cohere_api_key_here
```

> Get your free Groq key at [console.groq.com](https://console.groq.com) and Cohere key at [cohere.com](https://cohere.com).

### 5. Build the FAISS index (first time only)

```bash
python embeddings.py
```

### 6. Run the app

```bash
python app.py
```

Visit `http://localhost:8080` in your browser.

---

## 💬 Example Queries

```
✅ "How much protein do I need to build muscle?"
✅ "Create a 5-day workout split for fat loss"
✅ "What should I eat before and after a workout?"
✅ "How to increase my bench press?"
✅ "Is creatine safe for beginners?"

❌ "What's the capital of France?" → (Redirected — not fitness-related)
```

## 🌟 Fitness Influencers — The Inspiration Behind the Coach

The AI fitness coach in this app is trained on knowledge inspired by the training philosophies, nutrition guidance, and workout principles of these five incredible creators. Hours of their YouTube content shaped the thinking behind this chatbot's knowledge base.

<br>

<div align="center">

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| <img src="https://i.redd.it/max-euceda-22-years-old-59-185lbs-claims-science-based-v0-zkznkzdqeygc1.png?width=336&format=png&auto=webp&s=e7a0c76f4ea0e25efe5607d539f845f76d78530b" width="120" height="120" style="border-radius:50%;object-fit:cover" alt="Max Euceda"/> | <img src="https://www.optimumnutrition.co.in/cdn/shop/files/GWP05558.webp?v=1760004676" width="120" height="120" style="border-radius:50%;object-fit:cover" alt="Jeet Selal"/> | <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBVWU0nTnZot6Ezp09RLXFnXWgYzd5NHQF6w&s" width="120" height="120" style="border-radius:50%;object-fit:cover" alt="Saket Gokhle"/> | <img src="https://images.squarespace-cdn.com/content/v1/64c8035f53e9a56246c7c294/802d2e1f-82e7-4809-acee-b8aeb9b04b13/Jeff-Nippard.png" width="120" height="120" style="border-radius:50%;object-fit:cover" alt="Jeff Nippard"/> | <img src="https://preview.redd.it/a-day-in-life-of-a-bodybuilder-yatinder-singh-v0-oz5kdstxsxx21.jpg?width=800&format=pjpg&auto=webp&s=ce04e98179331f199cff5c4d29f258741ce6d753" width="120" height="120" style="border-radius:50%;object-fit:cover" alt="Yatinder Singh"/> |
| **[Max Euceda](https://www.youtube.com/@MaxEuceda7)** | **[Jeet Selal](https://www.youtube.com/c/JeetSelalAesthetics)** | **[Saket Gokhle](https://www.youtube.com/@SaketGokhaleVlogs)** | **[Jeff Nippard](https://www.youtube.com/@JeffNippard)** | **[Yatinder Singh](https://www.youtube.com/@YatinderSinghOfficial)** |
| 🇺🇸 Calisthenics & Aesthetics | 🇮🇳 Natural Bodybuilding & Diet | 🇮🇳 Fitness, Lifestyle & Fat Loss | 🇨🇦 Science-Based Strength Training | 🇮🇳 Mr. Asia · Powerlifting & Motivation |
| [![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=flat-square&logo=youtube)](https://www.youtube.com/@MaxEuceda) | [![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=flat-square&logo=youtube)](https://www.youtube.com/@JeetSelal) | [![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=flat-square&logo=youtube)](https://www.youtube.com/@SaketGokhle) | [![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=flat-square&logo=youtube)](https://www.youtube.com/@JeffNippard) | [![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=flat-square&logo=youtube)](https://www.youtube.com/@YatinderSingh) |

</div>

<br>

---


## 📦 Dependencies

```txt
flask==3.0.2
langchain==0.2.17
langchain-community==0.2.18
langchain-groq==0.1.10
langchain-cohere
cohere
faiss-cpu==1.13.2
numpy==1.26.4
pydantic==1.10.13
python-dotenv==1.0.1
```

---

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | API key for Groq LLM inference |
| `COHERE_API_KEY` | API key for Cohere embeddings |

---

## 🧪 Testing the RAG Pipeline

```bash
python test_rag.py
```

This runs a standalone test of the retriever and verifies that relevant document chunks are returned for sample fitness queries.

---

## 🚧 Known Limitations

- Session memory resets on server restart (no persistent storage)
- Domain filter uses keyword matching — edge cases may slip through
- Knowledge base quality directly impacts answer accuracy

---

## 🛣️ Future Roadmap

- [ ] User authentication & persistent chat history
- [ ] BMI / calorie calculator integrated into chat
- [ ] Personalized workout plan generator
- [ ] Voice input support
- [ ] Mobile-first UI redesign
      
## Mobile and Web PWA App Made at : 
https://github.com/Aadityayadav333/Health-Tracker-PWA/blob/main/README.md

---

<div align="center">

**⭐ Star this repo if it helped you build something awesome!**

</div>
