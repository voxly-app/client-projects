# Simple Chat Bot

This is a minimal chat bot web app you can embed into any website, or use as a starting point for building a smarter bot.

## ✅ What you get

- A **Flask backend** (`/api/chat`) that accepts chat messages and returns a reply
- A **single-page front end** (`templates/index.html`) that sends messages and renders the conversation
- A very simple **rule-based response engine** in `app.py` (easy to replace with OpenAI / Hugging Face / your own model)

## 🚀 Run locally

1) Create a Python virtual environment (recommended):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2) Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3) Run the app:

   ```powershell
   python app.py
   ```

4) Open in your browser:

   - http://localhost:5000

## 🧠 Making it smarter

### Option A: Use OpenAI (GPT)

1) Install `openai`:

```powershell
pip install openai
```

2) Set `OPENAI_API_KEY` in your environment.

3) Replace `get_response()` in `app.py` with an OpenAI call.

### Option B: Use a local model (e.g. Hugging Face)

You can replace the rule-based `get_response()` logic with any model inference code.

## 📦 Embedding in another website

To embed this bot in another site, either:

1) Run this service separately and call `/api/chat` from your site.
2) Copy the HTML/JS UI and point it to the `/api/chat` endpoint on whatever host you deploy to.

---

Enjoy building! 🎉
