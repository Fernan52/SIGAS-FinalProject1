from pymongo import MongoClient

client = MongoClient("mongodb+srv://moranavraham11:AW9ta2zrTeZiWdSh@cluster0.dogxq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shopping_cart

db.products.delete_many({})

products = [
    # Fruits
    {"name": "Apple", "category": "Fruits", "price": 2, "img": "/images/apple.jpg"},
    {"name": "Banana", "category": "Fruits", "price": 1, "img": "/images/banana.jpg"},
    {"name": "Pineapple", "category": "Fruits", "price": 4, "img": "/images/pineapple.jpg"},
    {"name": "Orange", "category": "Fruits", "price": 3, "img": "/images/orange.jpg"},
    {"name": "Strawberries", "category": "Fruits", "price": 6, "img": "/images/Strawberries.jpg"},

    # Vegetables
    {"name": "Tomato", "category": "Vegetables", "price": 2, "img": "/images/tomato.jpg"},
    {"name": "Cucumber", "category": "Vegetables", "price": 1.5, "img": "/images/cucumber.jpg"},
    {"name": "Orange pepper", "category": "Vegetables", "price": 3, "img": "/images/OrangePepper.jpg"},
    {"name": "Red pepper", "category": "Vegetables", "price": 3, "img": "/images/RedPepper.jpg"},
    {"name": "Yellow pepper", "category": "Vegetables", "price": 3, "img": "/images/YellowPepper.jpg"},

    # Snacks
    {"name": "Chips", "category": "Snacks", "price": 3, "img": "/images/chips.jpg"},
    {"name": "Cookies", "category": "Snacks", "price": 4, "img": "/images/cookies.jpg"},

    # Beverages
    {"name": "Water", "category": "Beverages", "price": 3, "img": "/images/Water.jpg"},
    {"name": "Juice", "category": "Beverages", "price": 4, "img": "/images/Juice.jpg"},
    {"name": "Soda", "category": "Beverages", "price": 2, "img": "/images/Soda.jpg"},
    {"name": "Coffee", "category": "Beverages", "price": 1.5, "img": "/images/Coffee.jpg"},
    {"name": "Tea", "category": "Beverages", "price": 1.5, "img": "/images/Tea.jpg"},

    # Meat
    {"name": "Chicken", "category": "Meat", "price": 3, "img": "/images/Chicken.jpg"},
    {"name": "Beef", "category": "Meat", "price": 4, "img": "/images/Beef.jpg"},
    {"name": "Fish", "category": "Meat", "price": 2, "img": "/images/Fish.jpg"},
    {"name": "Sausage", "category": "Meat", "price": 1.5, "img": "/images/Sausage.jpg"},

    # Dairy
    {"name": "Cheese", "category": "Dairy", "price": 3, "img": "/images/Cheese.jpg"},
    {"name": "Milk", "category": "Dairy", "price": 4, "img": "/images/Milk.jpg"},
    {"name": "Butter", "category": "Dairy", "price": 2, "img": "/images/Butter.jpg"},
    {"name": "Yogurt", "category": "Dairy", "price": 1.5, "img": "/images/Yogurt.jpg"},

    # Bakery
    {"name": "Bread", "category": "Bakery", "price": 3, "img": "/images/Bread.jpg"},
    {"name": "Croissant", "category": "Bakery", "price": 2, "img": "/images/Croissant.jpg"},
    {"name": "Muffin", "category": "Bakery", "price": 1.5, "img": "/images/Muffin.jpg"},

    # Frozen
    {"name": "Frozen Peas", "category": "Frozen", "price": 3, "img": "/images/FrozenPeas.jpg"},
    {"name": "Frozen Pizza", "category": "Frozen", "price": 4, "img": "/images/FrozenPizza.jpg"},

    # Cleaning
    {"name": "Bleach", "category": "Cleaning", "price": 3, "img": "/images/Bleach.jpg"},
    {"name": "Soap", "category": "Cleaning", "price": 4, "img": "/images/Soap.jpg"},
    {"name": "Shampoo", "category": "Cleaning", "price": 2, "img": "/images/Shampoo.jpg"},

    # Baby
    {"name": "Diapers", "category": "Baby", "price": 3, "img": "/images/Diapers.jpg"},
    {"name": "Baby Wipes", "category": "Baby", "price": 4, "img": "/images/BabyWipes.jpg"},
]

result = db.products.insert_many(products)

print(f"Inserted {len(result.inserted_ids)} products into the database.")

purchase_history = [
    {"username": "user1", "product_name": "Apple", "quantity": 3, "price": 6, "date": "2025-02-10"},
    {"username": "user1", "product_name": "Banana", "quantity": 2, "price": 2, "date": "2025-02-11"},
    {"username": "user2", "product_name": "Milk", "quantity": 1, "price": 4, "date": "2025-02-10"},
]

db.purchase_history.delete_many({})
db.purchase_history.insert_many(purchase_history)

print(f"Inserted {len(purchase_history)} purchase history records into the database.")
