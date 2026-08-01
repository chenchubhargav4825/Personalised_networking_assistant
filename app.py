import streamlit as st
import google.generativeai as genai
import wikipedia
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤝 Personalized Networking Assistant")

# -------------------------
# Conversation Starter
# -------------------------

st.header("Conversation Starter")

name = st.text_input("Enter Your Name")
event = st.text_area("Enter Event Description")
interest = st.text_input("Enter Your Interests")

if st.button("Generate AI Conversation Starter"):

    prompt = f"""
    User Name:{name}
    Event:{event}
    Interest:{interest}

    Generate 3 professional networking conversation starters.
    """

    response = model.generate_content(prompt)

    st.subheader("AI Generated Conversation Starters")
    st.write(response.text)

# -------------------------
# Fact Verification
# -------------------------

st.divider()

st.header("Quick Fact Verification")

topic = st.text_input("Enter a Topic")

if st.button("Verify Fact"):

    try:
        summary = wikipedia.summary(topic, sentences=3)

        st.success("Wikipedia Summary")
        st.write(summary)

    except Exception as e:
        st.error(f"Error: {e}")