from database import app, db, ma
from flask import jsonify, request

@app.route("/")
@app.route("/home")
def index():
    return jsonify({"hello":"World"})

@app.route('/get_item/<id>', methods = ['GET'])
def get_item(id):
    item = db.Item.query.get(id)
    return ma.item_schema.jsonify(item), 200

@app.route('/get_items', methods = ['GET'])
def get_items():
    all_items = db.Item.query.all()
    results = ma.items_schema.dump(all_items)
    return jsonify(results), 200

@app.route('/add_item', methods = ['POST'])
def add_item():
    name = request.json['name']
    price = request.json['price']
    description = request.json['description']
    stock = request.json['stock']
    image = request.json['image']

    new_item = db.Item(name=name, price=price, description=description, stock=stock, image=image)

    db.session.add(new_item)
    db.session.commit()

    return ma.item_schema.jsonify(new_item), 201

@app.route('/update_item/<id>', methods = ['PUT'])
def update_item(id):
    item = db.Item.query.get(id)

    name = request.json['name']
    price = request.json['price']
    description = request.json['description']
    stock = request.json['stock']
    image = request.json['image']

    item.name=name
    item.price=price 
    item.description=description
    item.stock=stock
    item.image=image

    db.session.commit()
    return ma.item_schema.jsonify(item), 201