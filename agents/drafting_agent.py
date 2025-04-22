from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
import os

def get_drafting_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.5,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

def draft_answer(llm, research_output):
    messages = [
        SystemMessage(content="You are an expert analyst. Draft a well-organized summary from the following information."),
        HumanMessage(content=research_output)
    ]
    return llm(messages).content 
