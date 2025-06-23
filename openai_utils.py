# openai_utils.py

from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = os.getenv("TOGETHER_MODEL")
API_KEY = os.getenv("TOGETHER_AI_API_KEY")  # ✅ this is what should be used for auth

def get_bios_with_together(prompt):
    response = completion(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        api_base="https://api.together.xyz/v1",
        api_key=API_KEY,  # ✅ Correct key here
        custom_llm_provider="together_ai"
    )
    return response['choices'][0]['message']['content']
