from flask import Flask, request, jsonify, render_template
from generator import generate_npc, get_field_data
import os

ENV = os.environ.get("ENV") or "dev"

app = Flask(__name__)


@app.route("/")
def api_details():
    return "Hello, world!"


@app.route("/generate-npc")
def generate_npc_data():
    field_data = get_field_data()
    return render_template("generate_npc.html", field_data=field_data)


@app.route("/api/generate-npc", methods=["GET", "POST"])
def create_npc():
    try:
        new_npc = generate_npc(request.args)
        if request.headers.get("X-Display-Format") == "html":
            npc_html = render_template("npc.html", new_npc=new_npc)
            return jsonify({
                'html_content': npc_html
            }), 200
        return jsonify(new_npc), 200
    except ValueError as e:
        print(f"Validation Error: {e}")
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=ENV == "dev")
