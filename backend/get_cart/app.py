from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for everyone

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI", "mongodb://SIGASDB:admin@mongo_service:27017/shopping_cart?authSource=admin")
client = MongoClient(mongo_uri)
db = client.shopping_cart

@app.route('/get_cart/<username>', methods=['GET'])
def get_cart(username):
    # Find the user by username
    user = db.users.find_one({"username": username})
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Return the user's cart
    cart = user.get("cart", [])  # Return the cart field, or an empty list if not found
    return jsonify({"username": username, "cart": cart}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4005)