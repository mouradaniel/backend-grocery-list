from flask import Blueprint, jsonify, request, Response
from db import Db
from bson import ObjectId

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

@itemsRoute.route('/items', methods=['GET'])
def list():
  list = db.list.find()
  items = []

  for item in list:
    item['_id'] = str(item['_id'])
    items.append(item)

  return jsonify(items)

@itemsRoute.route('/items/<id>', methods=['GET'])
def item(id):
  item = db.list.find_one({"_id": ObjectId(id)})
  item['_id'] = str(item['_id'])

  return jsonify(item)

@itemsRoute.route('/items/<id>', methods=['PATCH'])
def update(id):
  payload = request.json

  item = {
    "title": payload.get('title'), 
    "quantity": payload.get('quantity'), 
    "observation": payload.get('observation')
  }

  item = db.list.update_one({"_id": ObjectId(id)}, item)
  item['_id'] = str(item['_id'])

  return jsonify(item)

@itemsRoute.route('/items/<id>', methods=["DELETE"])
def remove(id):
  item = db.list.find_one_and_delete({"_id": ObjectId(id)})
  item['_id'] = str(item['_id'])

  return Response(status=201)