from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app) # Allows your HTML file to communicate with this server

DB_FILE = 'database.json'

def load_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(load_db())

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    users = load_db()
    users.append(new_user)
    save_db(users)
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)