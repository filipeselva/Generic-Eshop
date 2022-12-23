from datetime import datetime
from database import db

class user(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(lenght=30), nullable=False, unique=True)
    email_address = db.Column(db.String(lenght=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(lenght=60), nullable=False)
    adress = db.Column(db.String(lenght=120), nullable=False)
    postal_code = db.Column(db.String(lenght=60), nullable=False)
    mobile = db.Column(db.String(lenght=20), nullable=False)    
    budget = db.Column(db.Integer(), nullable=False, default=100)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
        

class item(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(lenght=30), nullable=False, unique=True)
    price = db.Column(db.Int(), nullable=False)
    Description = db.Column(db.String(lenght=60), nullable=False)
    stock = db.Column(db.Integer(), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Item. {self.name}'

class order(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Integer(), nullable=False)
    user = db.relationship('user', backref='user', lazy=True)
    

class order_item(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    order = db.relationship('order', backref='order', lazy=True)
    item = db.relationship('item', backref='item', lazy=True)
    item_price = db.Column(db.Int(), nullable=False)
    amount = db.Column(db.Integer(), nullable=False)

