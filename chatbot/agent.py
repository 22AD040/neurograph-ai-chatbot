import streamlit as st
import google.generativeai as genai

def run_agent(messages):
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("❌ GEMINI_API_KEY missing")
        return "API key error"

    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = "\n".join([m["role"] + ": " + m["content"] for m in messages])

    response = model.generate_content(prompt)

    return response.text