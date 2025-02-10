from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for everyone

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI", "mongodb://SIGASDB:admin@mongo_service:27017/shopping_cart?authSource=admin")
client = MongoClient(mongo_uri)
db = client.shopping_cart

@app.route('/search_products', methods=['GET'])
def search_products():
    category = request.args.get("query", "")  # Retrieve the category from the query string
    if category:
        products = list(db.products.find({"category": category}))  # Filter by category
    else:
        products = list(db.products.find())  # If no category is provided, return all products

    # Convert ObjectId to string for JSON compatibility
    for product in products:
        product["_id"] = str(product["_id"])
    
    return jsonify(products), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4009)