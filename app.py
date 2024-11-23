from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient

# Flask App
app = Flask(__name__, static_folder='static')

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")

# Databases
user_db = client["user_database"]
watch_db = client["watch_shop"]

# Collections
users_collection = user_db["users"]
products_collection = watch_db["products"]

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Get form data from the request
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return render_template('login.html', error="Please enter both username and password.")

    # Check if the user exists in the database
    user = users_collection.find_one({"username": username, "password": password})

    if user:
        # Login successful, redirect to index
        return redirect(url_for('index'))
    else:
        # Login failed, show an error message
        return render_template('login.html', error="Invalid username or password.")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Check if user already exists
        if users_collection.find_one({"username": username}):
            return jsonify({"message": "Username already exists"}), 400

        # Insert new user
        users_collection.insert_one({"username": username, "email": email, "password": password})
        return redirect(url_for('home'))

    return render_template('signup.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')

        # Check if email exists
        user = users_collection.find_one({"email": email})
        if user:
            return jsonify({"message": "Password reset link sent!"})
        return jsonify({"message": "Email not found"}), 404

    return render_template('forgot_password.html')

@app.route('/index')
def index():
    try:
        # Fetch products from the correct database
        products = list(products_collection.find({}, {"_id": 0}))  # Exclude `_id` field for cleaner output
        return render_template('index.html', products=products)
    except Exception as e:
        # Handle errors gracefully
        print(f"Error: {e}")
        return f"An error occurred: {e}", 500
# Add a new collection for orders
orders_collection = watch_db["orders"]

@app.route('/place_order', methods=['POST'])
def place_order():
    try:
        # Save order to the database
        order_data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "watch_name": request.form.get("watch_name"),
            "price": request.form.get("price"),
            "payment_method": request.form.get("payment_method"),  # Capture payment method
            "status": "Pending"  # Default status
        }
        orders_collection.insert_one(order_data)
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error placing order: {e}")
        return f"An error occurred: {e}", 500

@app.route('/admin/orders')
def admin_orders():
    try:
        # Fetch all orders for admin view
        orders = list(orders_collection.find({}, {"_id": 0}))  # Exclude _id for cleaner output
        return render_template('admin_orders.html', orders=orders)
    except Exception as e:
        print(f"Error fetching orders: {e}")
        return f"An error occurred: {e}", 500

@app.route('/admin/update_order', methods=['POST'])
def update_order():
    try:
        # Update the status of an order
        email = request.form.get("email")
        status = request.form.get("status")
        orders_collection.update_one({"email": email}, {"$set": {"status": status}})
        return redirect(url_for('admin_orders'))
    except Exception as e:
        print(f"Error updating order: {e}")
        return f"An error occurred: {e}", 500


if __name__ == '__main__':
    app.run(debug=True)
