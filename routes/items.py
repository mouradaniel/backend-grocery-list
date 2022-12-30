from flask import Blueprint, jsonify, request
from db import Db

itemsRoute = Blueprint('transfer', __name__)

db = Db.Connect()

@itemsRoute.route('/items', methods=["POST"])
def create():
  payload = request.json

  item = {
    "title": payload.get('title'), 
    "quantity": payload.get('quantity'), 
    "observation": payload.get('observation')
  }

  db.list.insert_one(item)
  item['_id'] = str(item['_id'])

  return jsonify(item)
