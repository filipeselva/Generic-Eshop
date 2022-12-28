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

@app.route('/get_all_items', methods = ['GET'])
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
    db.session.remove()

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
    db.session.remove()
    return ma.item_schema.jsonify(item), 201

@app.route('/delete_item/<id>', methods = ['DELETE'])
def delete_item(id):
    item = db.Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    db.session.remove()
    return ma.item_schema.jsonify(item)

@app.route('/add_user', methods = ['POST'])
def add_user():
    pass #Will do it when have the authentication know-how.

@app.route('/get_user/<id>', methods = ['GET'])
def get_user(id):
    user = db.User.query.get(id)
    return ma.user_schema.jsonify(user), 200

@app.route('/get_all_users', methods = ['GET'])
def get_users():
    all_users = db.Item.query.all()
    results = ma.users_schema.dump(all_users)
    return jsonify(results), 200

@app.route('/update_user/<id>', methods = ['PUT'])
def update_user(id):
    user = db.User.query.get(id)

    email_adress = request.json['email_adress']
    adress = request.json['adress']
    postal_code = request.json['postal_code']
    mobile = request.json['mobile']
    
    user.email_adress=email_adress
    user.adress=adress 
    user.postal_code=postal_code
    user.mobile=mobile
    
    db.session.commit()
    db.session.remove()
    return ma.user_schema.jsonify(user), 201

@app.route('/update_user_budget/<id>', methods = ['PUT'])
def update_user_budget(id):
    user = db.User.query.get(id)
    budget = request.json['budget']
    user.budget=budget
    db.session.commit()
    db.session.remove()
    return ma.user_schema.jsonify(user), 201

@app.route('/delete_user/<id>', methods = ['DELETE'])
def delete_user(id):
    user = db.User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    db.session.remove()
    return ma.user_schema.jsonify(user)