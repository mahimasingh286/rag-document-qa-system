from flask import Flask, request, jsonify
from rag import ask_question

app = Flask(__name__)


@app.route("/")
def home():
    return "Flask running"


@app.route("/ask")
def ask():

    q = request.args.get("q")

    if not q:
        return jsonify({"error": "No question"})

    ans = ask_question(q)

    return jsonify({"answer": ans})


if __name__ == "__main__":
    app.run(debug=True)