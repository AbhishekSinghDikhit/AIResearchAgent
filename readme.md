# 🧠 Dual-Agent AI Research System

A powerful, multi-agent AI system for deep research tasks using real-time web search and advanced language generation. This project combines the capabilities of **Tavily**, **Gemini (via LangChain)**, **LangGraph**, and a clean **Streamlit** UI to provide a human-like research assistant that gathers and summarizes web data intelligently.

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

```text
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

Research Agent: Gathers information by performing real-time web searches through Tavily.

Drafting Agent: Analyzes and summarizes collected data using Gemini LLM to produce structured, human-readable outputs.

Streamlit UI: Allows users to input queries and view detailed research results interactively.
