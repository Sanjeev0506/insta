# ✅ Imports
import streamlit as st
from prompt_template import build_prompt
from openai_utils import get_bios_with_together as get_bios_from_openai
import os

# ✅ Streamlit page config
st.set_page_config(page_title="Instagram Bio Generator", layout="centered")

# ✅ Load custom CSS (Professional Style)
css_path = "style.css"
with open(css_path) as f:
    css_content = f.read()
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# ✅ Header Section
st.markdown("""
<div class="instagram-header">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" alt="Instagram Logo" width="20" height="20">
    <span>Instagram Bio Generator</span>
</div>
""", unsafe_allow_html=True)

# ✅ Input Section
keywords = st.text_input("Enter keywords (comma-separated)", placeholder="e.g., travel, coffee, books")

tone = st.radio("Choose a vibe or tone", [
    "Funny", "Aesthetic", "Minimal", "Professional", "Romantic",
    "Bold", "Dark", "Soft", "Wholesome", "Sarcastic"
], horizontal=True)

bio_length = st.slider("Bio length (characters)", 20, 150, 100)

# ✅ Generate Button
if st.button("🚀 Generate Bio"):
    if not keywords.strip():
        st.warning("Please enter at least one keyword.")
    else:
        with st.spinner("Generating bios..."):
            try:
                prompt = build_prompt(keywords, tone, bio_length)
                result = get_bios_from_openai(prompt)
                bios = [line.strip("-• \n") for line in result.strip().split("\n") if line.strip()]
                
                st.subheader("🎯 Your Bios:")
                for bio in bios:
                    st.code(bio, language="markdown")
            except Exception as e:
                st.error(f"Error: {e}")
