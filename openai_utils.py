from litellm import completion
import streamlit as st  # ✅ Needed for st.secrets

MODEL = st.secrets["TOGETHER_MODEL"]
API_KEY = st.secrets["TOGETHER_AI_API_KEY"]

def get_bios_with_together(prompt):
    response = completion(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        api_base="https://api.together.xyz/v1",
        api_key=API_KEY,
        custom_llm_provider="together_ai"
    )
    return response['choices'][0]['message']['content']
