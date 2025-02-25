"""
User Management Module
This module handles basic user authentication and session management for the dashboard.
"""

from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

users = {
    "user1": "password1",
    "user2": "password2"
}

def generate_token(username):
    token = jwt.encode(
        {"username": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
        app.config['SECRET_KEY'],
        algorithm="HS256"
    )
    return token

@app.route('/api/v1/users/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if username in users and users[username] == password:
        token = generate_token(username)
        return jsonify({"token": token})
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
