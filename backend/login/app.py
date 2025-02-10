from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from pymongo import MongoClient
from werkzeug.security import check_password_hash

app = Flask(__name__)
CORS(app)  # Enable CORS for everyone

client = MongoClient("MONGO_URI=mongodb://SIGASDB:admin@mongo_service:27017/shopping_cart?authSource=admin")
db = client.shopping_cart

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    # Find the user in the database
    user = db.users.find_one({"username": username})
    if user and check_password_hash(user["password"], password):
        # Return a successful response with the username
        return jsonify({"message": "Login successful", "username": username}), 200

    # Return an error if login fails
    return jsonify({"error": "Invalid username or password"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4006)
