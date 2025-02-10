from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# Obtener la URI de MongoDB desde las variables de entorno
mongo_uri = os.getenv("MONGO_URI", "mongodb://SIGASDB:admin@mongo_service:27017/shopping_cart?authSource=admin")
client = MongoClient(mongo_uri)
db = client.shopping_cart

@app.route('/get_products', methods=['GET'])
def get_products():
    category = request.args.get('category', None)
    if category:
        products = list(db.products.find({"category": category}))
    else:
        products = list(db.products.find())
    for product in products:
        product["_id"] = str(product["_id"])
    return jsonify(products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4012)