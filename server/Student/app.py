from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)  # Enables frontend requests

DATA_FILE = "students.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify(load_data())

@app.route("/api/students", methods=["POST"])
def add_student():
    data = load_data()
    student = request.json
    data[student["id"]] = student["details"]
    save_data(data)
    return jsonify({"message": "Student saved!"}), 201

if __name__ == "__main__":
    app.run(port=5000, debug=True)