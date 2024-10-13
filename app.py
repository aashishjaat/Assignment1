from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://karangoswami0001:karan231299@cluster0.o0fs8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shop_db
products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products_data = list(products_collection.find())
    return render_template('products.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True)
