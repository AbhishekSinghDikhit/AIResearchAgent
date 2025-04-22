import streamlit as st
from agents.research_agent import web_research_tool
from agents.drafting_agent import get_drafting_llm, draft_answer
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Research Agent", layout="centered")
st.title("🔍 Deep Research AI Agent")

query = st.text_input("Enter your research query:")

if st.button("Start Research") and query:
    with st.spinner("Researching the web..."):
        research_result = web_research_tool.run(query)
        st.success("Web Research Completed")
        st.subheader("📚 Research Summary")
        st.markdown(research_result)

    with st.spinner("Drafting answer with Gemini..."):
        llm = get_drafting_llm()
        final_answer = draft_answer(llm, research_result)
        st.success("Drafting Completed")
        st.subheader("✍️ Final Answer")
        st.markdown(final_answer)
