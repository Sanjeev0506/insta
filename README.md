
# 📸 Instagram Bio Generator

Effortlessly generate unique, catchy, or aesthetic Instagram bios powered by AI.

---

## ✨ **Features**

✅ AI-powered bio generation using **Together AI models**  
✅ Customize bios based on your **keywords**, **tone**, and **length**  
✅ Clean, professional web interface built with **Streamlit**  
✅ Mobile-responsive and minimal UI  
✅ Generates multiple bio suggestions instantly  

---

## ⚡ **Tech Stack**

- **Python 3.9+**  
- **Streamlit** (for web interface)  
- **Together AI** (LLM for generating bios)  
- **Litellm** (API integration)  
- **dotenv** (for secure API key management)  
- **Custom CSS** for a modern, professional design  

---

## 🛠️ **Installation**

1. **Clone the repository**

```bash
git clone https://github.com/your-username/instagram-bio-generator.git
cd instagram-bio-generator
```

2. **Create and activate virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Setup `.env` file**

Create a `.env` file in the root directory with:

```
TOGETHER_MODEL=togethercomputer/llama-3-70b-chat
TOGETHER_AI_API_KEY=your_actual_api_key_here
```

Alternatively, use **Streamlit Cloud Secrets** for deployment.

---

## 🚀 **Usage**

Run the app locally:

```bash
streamlit run app.py
```

The app will open in your browser.

---

## 🌐 **Live Demo**

> [Optional] Add your deployed app link here once deployed on Streamlit Cloud.

---

## 🎨 **Screenshots**

> [Optional] Add screenshots or a screen recording of your app here.

---

## 🔒 **Security Notes**

✅ `.env` is excluded via `.gitignore` — never commit your API keys.  
✅ For Streamlit Cloud, use **Secrets Manager** with correct TOML formatting.

---

## 🤖 **AI Model**

This project uses **Together AI** models via **Litellm** integration to generate bios based on your prompt.

---

## 📂 **Project Structure**

```
instagram-bio-generator/
├── app.py
├── openai_utils.py
├── prompt_template.py
├── style.css
├── requirements.txt
├── .streamlit/
│   └── config.toml
└── .env  (excluded from GitHub)
```

---

## 💡 **Future Improvements**

- Add copy-to-clipboard functionality  
- Bio style previews before generating  
- More tones & styles  
- Additional social media platform support  

---

## 🤝 **Contributing**

Contributions and suggestions are welcome!  
Feel free to fork this project and create a pull request.

---

## 📄 **License**

This project is licensed under the [MIT License](LICENSE).
