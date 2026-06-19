from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load dataset from JSON file
with open("data/universities.json") as f:
    universities = json.load(f)

# Route: Get all universities
@app.route("/universities", methods=["GET"])
def get_universities():
    return jsonify(universities)

# Route: Get a single university by slug
@app.route("/universities/<slug>", methods=["GET"])
def get_university(slug):
    uni = next((u for u in universities if u["slug"] == slug), None)
    if uni:
        return jsonify(uni)
    return jsonify({"error": "University not found"}), 404

# Route: Filter universities by type (Federal, State, Private)
@app.route("/universities/type/<uni_type>", methods=["GET"])
def get_universities_by_type(uni_type):
    filtered = [u for u in universities if u["type"].lower() == uni_type.lower()]
    return jsonify(filtered)

if __name__ == "__main__":
    app.run(debug=True)
