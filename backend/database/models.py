from datetime import datetime
from database import db

class OrderItem(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    item_id = db.Column(db.Integer(), db.ForeignKey('item.id'))
    item_price = db.Column(db.Integer(), nullable=False)
    amount = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'Item. {self.id}'

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    email_address = db.Column(db.String(60), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    adress = db.Column(db.String(120), nullable=False)
    postal_code = db.Column(db.String(60), nullable=False)
    mobile = db.Column(db.String(20), nullable=False)    
    budget = db.Column(db.Integer(), nullable=False, default=100)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    orders = db.relationship('Order', backref='user', lazy=True)

    def __repr__(self):
        return f'Item. {self.id}'

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    stock = db.Column(db.Integer(), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    order_item_id = db.Column(db.Integer(), db.ForeignKey('order_item.id'))

    def __repr__(self):
        return f'Item. {self.name}'

class Order(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    order_items = db.relationship('OrderItem', backref='order', lazy=True)
    status = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'Item. {self.id}'