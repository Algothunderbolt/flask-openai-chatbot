from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if user_message == "":
        return jsonify({"reply": "Please say something."})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a friendly helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    bot_reply = response.choices[0].message.content

    return jsonify({"reply": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)



