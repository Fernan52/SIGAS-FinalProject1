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
    {"name": "Strawberries", "category": "Fruits", "price": 6, "img": "/images/strawberries.jpg"},

    # Vegetables
    {"name": "Tomato", "category": "Vegetables", "price": 2, "img": "/images/tomato.jpg"},
    {"name": "Cucumber", "category": "Vegetables", "price": 1.5, "img": "/images/cucumber.jpg"},
    {"name": "Orange pepper", "category": "Vegetables", "price": 3, "img": "/images/orange_pepper.jpg"},
    {"name": "Red pepper", "category": "Vegetables", "price": 3, "img": "/images/red_pepper.jpg"},
    {"name": "Yellow pepper", "category": "Vegetables", "price": 3, "img": "/images/yellow_pepper.jpg"},

    # Snacks
    {"name": "Chips", "category": "Snacks", "price": 3, "img": "/images/chips.jpg"},
    {"name": "Cookies", "category": "Snacks", "price": 4, "img": "/images/cookies.jpg"},

    # Beverages
    {"name": "Water", "category": "Beverages", "price": 3, "img": "/images/water.jpg"},
    {"name": "Juice", "category": "Beverages", "price": 4, "img": "/images/juice.jpg"},
    {"name": "Soda", "category": "Beverages", "price": 2, "img": "/images/soda.jpg"},
    {"name": "Coffee", "category": "Beverages", "price": 1.5, "img": "/images/coffee.jpg"},
    {"name": "Tea", "category": "Beverages", "price": 1.5, "img": "/images/tea.jpg"},

    # Meat
    {"name": "Chicken", "category": "Meat", "price": 3, "img": "/images/chicken.jpg"},
    {"name": "Beef", "category": "Meat", "price": 4, "img": "/images/beef.jpg"},
    {"name": "Fish", "category": "Meat", "price": 2, "img": "/images/fish.jpg"},
    {"name": "Sausage", "category": "Meat", "price": 1.5, "img": "/images/sausage.jpg"},

    # Dairy
    {"name": "Cheese", "category": "Dairy", "price": 3, "img": "/images/cheese.jpg"},
    {"name": "Milk", "category": "Dairy", "price": 4, "img": "/images/milk.jpg"},
    {"name": "Butter", "category": "Dairy", "price": 2, "img": "/images/butter.jpg"},
    {"name": "Yogurt", "category": "Dairy", "price": 1.5, "img": "/images/yogurt.jpg"},

    # Bakery
    {"name": "Bread", "category": "Bakery", "price": 3, "img": "/images/bread.jpg"},
    {"name": "Croissant", "category": "Bakery", "price": 2, "img": "/images/croissant.jpg"},
    {"name": "Muffin", "category": "Bakery", "price": 1.5, "img": "/images/muffin.jpg"},

    # Frozen
    {"name": "Frozen Peas", "category": "Frozen", "price": 3, "img": "/images/frozen_peas.jpg"},
    {"name": "Frozen Pizza", "category": "Frozen", "price": 4, "img": "/images/frozen_pizza.jpg"},

    # Cleaning
    {"name": "Bleach", "category": "Cleaning", "price": 3, "img": "/images/bleach.jpg"},
    {"name": "Soap", "category": "Cleaning", "price": 4, "img": "/images/soap.jpg"},
    {"name": "Shampoo", "category": "Cleaning", "price": 2, "img": "/images/shampoo.jpg"},

    # Baby
    {"name": "Diapers", "category": "Baby", "price": 3, "img": "/images/diapers.jpg"},
    {"name": "Baby Wipes", "category": "Baby", "price": 4, "img": "/images/baby_wipes.jpg"},
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
