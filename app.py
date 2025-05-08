from flask import Flask
from pymongo import MongoClient

client = MongoClient("mongodb+srv://alasylkhh:123@cluster0.6fmla.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['users']
users = db['users']
