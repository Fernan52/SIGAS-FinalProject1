from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import subprocess

app = Flask(__name__)
CORS(app)  # Enable CORS for everyone

try:
    client = MongoClient(
        "MONGO_URI=mongodb://SIGASDB:admin@mongo_service:27017/shopping_cart?authSource=admin"
    )
    db = client.shopping_cart

    @app.route('/add_product', methods=['POST'])
    def add_product():
        data = request.get_json()
        username = data.get("username")  
        product = {
            "name": data["name"],
            "category": data["category"],
            "price": data["price"],
            "quantity": data["quantity"]  
        }

        
        user = db.users.find_one({"username": username})
        if not user:
            return jsonify({"error": "User not found"}), 404

        
        db.users.update_one(
            {"username": username},
            {"$push": {"cart": product}}
        )

        return jsonify({"message": "Product added to user's cart successfully!"}), 200

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=4000)

except Exception as e:
    print(f"Flask service failed: {e}")
    print("Attempting to start the Node.js service...")
    try:
        # Start the Node.js service
        subprocess.run(["node", "node_service.js"], check=True)
    except Exception as node_error:
        print(f"Node.js service failed: {node_error}")
        print("Both services failed. Exiting.")
