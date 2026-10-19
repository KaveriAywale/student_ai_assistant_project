import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are a helpful Student AI Assistant for school and college students.
Explain academic concepts in simple, clear language. Keep answers organized and relevant.
For summaries, give the main points as bullets. For quiz requests, provide practice
questions and answers. If a question is unclear, ask for clarification. Never present
uncertain information as definitely true; suggest verification when appropriate.
Do not request unnecessary personal or confidential information."""

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"error": "Please enter a question or study task."}), 400
    if len(message) > 6000:
        return jsonify({"error": "Please keep your input under 6,000 characters."}), 400
    if not os.environ.get("OPENAI_API_KEY"):
        return jsonify({"error": "API key not configured. Set OPENAI_API_KEY and restart the app."}), 503
    try:
        response = client.responses.create(
            model=os.environ.get("OPENAI_MODEL", "gpt-4.1-mini"),
            instructions=SYSTEM_PROMPT,
            input=message,
            max_output_tokens=700
        )
        return jsonify({"answer": response.output_text})
    except Exception:
        app.logger.exception("AI request failed")
        return jsonify({"error": "The AI service could not complete the request. Check your API key, network, and model access."}), 502

if __name__ == "__main__":
    app.run(debug=True)
