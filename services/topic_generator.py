import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_conversation_starters(event, interests):

    prompt = f"""
You are an AI Networking Assistant.

Event:
{event}

User Interests:
{', '.join(interests)}

Generate exactly 3 professional networking conversation starters.

Return only the conversation starters.
"""

    response = model.generate_content(prompt)

    return response.text