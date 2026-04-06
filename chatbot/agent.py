import streamlit as st
import google.generativeai as genai
if "GEMINI_API_KEY" not in st.secrets:
    st.error("❌ GEMINI_API_KEY not found in secrets")
    st.stop()
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

def run_agent(messages):
    prompt = "\n".join([m["role"] + ": " + m["content"] for m in messages])
    response = model.generate_content(prompt)
    return response.text