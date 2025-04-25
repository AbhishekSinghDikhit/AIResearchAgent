# 🧠 Dual-Agent AI Research System

A powerful, multi-agent AI system for deep research tasks using real-time web search and advanced language generation. This project combines the capabilities of **Tavily**, **Gemini (via LangChain)**, **LangGraph**, and a clean **Streamlit** UI to provide a human-like research assistant that gathers and summarizes web data intelligently.

## Demo
- Demo Link : [Website](https://deepresearchai.streamlit.app/)
  
---

## 📌 Problem Statement

Design a Deep Research AI Agentic System that:
- Crawls websites using **Tavily**.
- Implements a **dual-agent architecture**:
  - One agent for research and data collection.
  - One agent for drafting coherent, insightful summaries.
- Utilizes **LangGraph** and **LangChain** for agent orchestration.
- Offers an interactive front-end for user interaction.

---

## 🧩 System Architecture

```
[ User Input (Query) ]
        |
        v
[ Research Agent 🧭 ]
  - Tavily Web Search API
        |
        v
[ Drafting Agent 📝 ]
  - Gemini LLM via LangChain
        |
        v
[ Streamlit UI Output 🎯 ]
```

- Research Agent: Gathers information by performing real-time web searches through Tavily.
- Drafting Agent: Analyzes and summarizes collected data using Gemini LLM to produce structured, human-readable outputs.
- Streamlit UI: Allows users to input queries and view detailed research results interactively.

## ⚙️ Features

- 🔍 Real-time Web Research: Fetches fresh, relevant information using Tavily’s search capabilities.
- 🤖 Dual-Agent Pipeline: Clear separation between research collection and summary drafting for better modularity and quality.
- 🧠 Structured Summarization: Gemini LLM drafts concise, referenced answers.
- 📚 History Tracking: Maintains session-based history of queries and results.
- 🖥️ Streamlit Frontend: Lightweight, intuitive interface with live progress indicators.
- 💾 Bookmark Important Research: Ability to bookmark and revisit important responses.


## 🚀 Installation
### 1. Clone the Repository
```
git clone https://github.com/AbhishekSinghDikhit/DeepResearchAI.git
cd DeepResearchAI
```

### 2. Create and Activate a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Set Environment Variables

- Create a .env file in the root directory and add:
```
TAVILY_API_KEY=your_tavily_api_key
GEMINI_API_KEY=your_gemini_api_key
```
(You can get free Tavily and Gemini API keys from their official sites.)

### 5. Run the App
```
streamlit run app.py
```
The app will be available at http://localhost:8501

## 🛠 Tech Stack

| Layer                 | Tools Used                 |
|-----------------------|----------------------------|
| Language Models       | Gemini (via LangChain)     |
| Search API            | Tavily Web Search API      |
| Agent Framework       | LangChain, LangGraph       |
| Frontend              | Streamlit                  |
| Environment Management| Python Dotenv              |

## 🧩 Core Components

| Component           | Description                                                                                                                                                  |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Research Agent      | Accepts the user query, performs multi-threaded web search via Tavily, gathers relevant articles and information.                                            |
| Drafting Agent      | Processes raw collected data and synthesizes a summarized, human-like draft with references using Gemini LLM.                                                |
| Agent Orchestration | Managed via LangGraph to ensure the flow between research and drafting agents is smooth and fault-tolerant.                                                  |
| Frontend UI         | Built with Streamlit to provide a simple, clean interface for users to input queries, view real-time research progress, and access history/bookmarks.        |

## 📋 Usage Guide

- Open the app and type a research query (e.g., "Future of renewable energy in India").
- Click Search.
-  Watch live progress:
      - The Research Agent fetches web content.
      - The Drafting Agent writes a structured summary.
- View results, complete with citations and references.
- Bookmark any important findings for later use.

## 📬 Contact

For any queries or feedback, feel free to reach out:

- GitHub: [AbhishekSinghDikhit](https://github.com/AbhishekSinghDikhit)
- Email: [aabhishek576@gmail.com](mailto:aabhishek576@gmail.com)



  
