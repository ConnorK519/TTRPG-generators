from flask import Flask, request, jsonify
from generator import generate_npc
import os

ENV = os.environ.get("ENV") or "dev"

app = Flask(__name__)


@app.route("/")
def api_details():
    return "Hello, world!"


@app.route("/generate-npc")
def get_npc_data():
    pass


@app.route("/api/generate-npc")
def create_npc():
    new_npc = generate_npc(request.args)
    return new_npc


if __name__ == "__main__":
    app.run(debug=ENV == "dev")
