from flask import Flask
from flask_pymongo import PyMongo
from os import environ

app = Flask(__name__)

class Db:
  def Connect():
    app.config["MONGO_URI"] = environ.get('MONGO_URI')
    mongo = PyMongo(app)
    db = mongo.db
    return db