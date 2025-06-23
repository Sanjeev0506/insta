from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = os.getenv("TOGETHER_MODEL")
API_KEY = os.getenv("TOGETHER_AI_API_KEY")

# Debug print to verify
print(f"Loaded MODEL: {MODEL}")
print(f"Loaded API KEY: {API_KEY[:4]}...")  # Don't print full key for security

def get_bios_with_together(prompt):
    response = completion(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        api_base="https://api.together.xyz/v1",
        api_key=API_KEY,
        custom_llm_provider="together_ai"
    )
    return response['choices'][0]['message']['content']
