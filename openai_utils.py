from litellm import completion
import os
import streamlit as st
from dotenv import load_dotenv

# Load .env for local development
load_dotenv()

# Fetch model and API key with fallback logic:
MODEL = st.secrets.get("TOGETHER_MODEL") or os.getenv("TOGETHER_MODEL")
API_KEY = st.secrets.get("TOGETHER_AI_API_KEY") or os.getenv("TOGETHER_AI_API_KEY")

def get_bios_with_together(prompt):
    if not MODEL or not API_KEY:
        raise ValueError("MODEL or API_KEY not set. Please check your environment variables or Streamlit Secrets.")

    response = completion(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        api_base="https://api.together.xyz/v1",
        api_key=API_KEY,
        custom_llm_provider="together_ai"
    )
    return response['choices'][0]['message']['content']
