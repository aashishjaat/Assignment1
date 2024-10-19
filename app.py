from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Fetching environment variables
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_CLUSTER_URL = os.getenv('MONGODB_CLUSTER_URL')

# MongoDB connection string using environment variables
client = MongoClient(f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER_URL}/?retryWrites=true&w=majority&appName=Cluster0")
db = client.Assignment1
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
