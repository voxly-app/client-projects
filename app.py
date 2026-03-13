from flask import Flask, request, jsonify, render_template
import os
import re

app = Flask(__name__, static_folder="static", template_folder="templates")

# --- Simple rule-based responder (starter) ---
# Replace or extend this with any NLP/ML model (OpenAI, Hugging Face, etc.)

def get_response(message: str) -> str:
    message = message.strip()
    if not message:
        return "Please say something so I can respond 😊"

    # Normalize to lowercase for simple pattern matching
    msg_lower = message.lower()

    # greetings
    if re.search(r"\b(hi|hello|hey|yo|greetings)\b", msg_lower):
        return "Hello! How can I help you today?"

    # ask about time
    if "time" in msg_lower:
        from datetime import datetime
        return f"It is currently {datetime.now().strftime('%I:%M %p')}"

    # ask about date
    if "date" in msg_lower:
        from datetime import datetime
        return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}"

    # simple math
    match = re.search(r"what is (\d+)\s*([+\-*/])\s*(\d+)", msg_lower)
    if match:
        a, op, b = int(match.group(1)), match.group(2), int(match.group(3))
        try:
            result = {
                "+": a + b,
                "-": a - b,
                "*": a * b,
                "/": a / b if b != 0 else "∞",
            }[op]
            return f"The answer is {result}"
        except Exception:
            pass

    return "I’m a simple bot right now. Try asking about the time, date, or say hi!"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat_api():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    reply = get_response(message)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
