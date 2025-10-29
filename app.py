from flask import Flask, request, jsonify
from generator import roll_race, check_race_exists, roll_genre, check_genre_exists, roll_gender, roll_class, generate_name, generate_stats

app = Flask(__name__)


@app.route("/")
def api_details():
    return "Hello, world!"


@app.route("/api/generate-npc")
def create_npc():
    return


if __name__ == "__main__":
    app.run(debug=True)
