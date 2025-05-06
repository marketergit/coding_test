# backend.py
from flask import Flask, request, jsonify
import requests
from groq import Client
import os

app = Flask(__name__)

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.environ.get("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")

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    user_message = data.get("message")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mixtral-8x7b-32768",  # or groq-compatible model
        "messages": [{"role": "user", "content": user_message}],
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    reply = response.json()["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
