# app.py

import streamlit as st
from prompt_template import build_prompt
from openai_utils import get_bios_with_together as get_bios_from_openai
import os

# Page Config - MUST be the first Streamlit command
st.set_page_config(page_title="InstaBio Generator", layout="centered")

# Load Custom CSS
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Custom Header with Instagram logo
st.markdown(
    """
    <h1 style='text-align: center;'>
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="30" style="vertical-align: middle; margin-right: 10px;">
        <span style="color: #e50914;">InstaBio Generator</span>
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("Generate unique Instagram bios based on your keywords and vibe. Powered by Together.ai")

# User Inputs
keywords = st.text_input("Enter keywords (comma-separated)", placeholder="e.g., travel, coffee, books")

tone = st.radio("Choose a vibe or tone", [
    "Funny", "Aesthetic", "Minimal", "Professional", "Romantic",
    "Bold", "Dark", "Soft", "Wholesome", "Sarcastic"
], horizontal=True)

bio_length = st.slider("Bio length (characters)", 20, 150, 100)

# Generate Button
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
# Streamlit app placeholder
