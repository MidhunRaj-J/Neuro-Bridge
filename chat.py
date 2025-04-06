from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
from dotenv import dotenv_values
from json import load, dump
import datetime
import os

app = Flask(__name__)
CORS(app)

# Load environment variables
env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")
Assistantname = env_vars.get("Assistantname", "NeuroBridge")

client = Groq(api_key=GroqAPIKey)

chatlog_path = "Data/ChatLog.json"
if not os.path.exists("Data"):
    os.makedirs("Data")
    with open(chatlog_path, "w") as f:
        dump([], f)

SystemPrompt = f"""
You are {Assistantname}, an AI communication assistant for people with speech or cognitive difficulties...

User: "no food"
Assistant: "I'm hungry and would like something to eat."

User: "pain leg bad"
Assistant: "I'm feeling severe pain in my leg."

Always respond with polite, clear English based on minimal or broken inputs.
"""

SystemMessages = [{"role": "system", "content": SystemPrompt}]

def get_time_info():
    now = datetime.datetime.now()
    return f"Day: {now.strftime('%A')}, Time: {now.strftime('%H:%M:%S')}"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        with open(chatlog_path, "r") as f:
            messages = load(f)

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=SystemMessages + [{"role": "system", "content": get_time_info()}] + messages,
            max_tokens=1024,
            temperature=0.7,
            stream=False
        )

        answer = response.choices[0].message.content.strip()
        messages.append({"role": "assistant", "content": answer})

        with open(chatlog_path, "w") as f:
            dump(messages, f, indent=2)

        return jsonify({"response": answer})

    except Exception as e:
        print("Error:", e)
        return jsonify({"response": "Sorry, something went wrong."}), 500

if __name__ == "__main__":
    app.run(debug=True)
