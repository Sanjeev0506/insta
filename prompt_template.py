# prompt_template.py

def build_prompt(keywords, tone, length):
    return f"""
Generate 3 unique Instagram bios based on:
- Keywords: {keywords}
- Tone: {tone}
- Max Length: {length} characters

Each bio should be creative, match the tone, and stay within the character limit.
Return only the bios as bullet points.
"""
