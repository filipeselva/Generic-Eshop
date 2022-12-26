from datetime import datetime
from database import db

class user(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    email_address = db.Column(db.String(lenght=60), nullable=False, unique=True)
    password_hash = db.Column(db.String(lenght=60), nullable=False)
    adress = db.Column(db.String(lenght=120), nullable=False)
    postal_code = db.Column(db.String(lenght=60), nullable=False)
    mobile = db.Column(db.String(lenght=20), nullable=False)    
    budget = db.Column(db.Integer(), nullable=False, default=100)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    order = db.relationship('order', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'Item. {self.id}'
        

class item(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(lenght=120), nullable=False, unique=True)
    price = db.Column(db.Int(), nullable=False)
    Description = db.Column(db.String(lenght=400), nullable=False)
    stock = db.Column(db.Integer(), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    order_item = db.Column(db.Integer(), db.ForeignKey())

    def __repr__(self):
        return f'Item. {self.name}'

class order(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Integer(), nullable=False)
    user = db.Column(db.Integer(), db.ForeignKey())
    order_item = db.Column(db.Integer(), db.ForeignKey())

    def __repr__(self):
        return f'Item. {self.id}'
    

class order_item(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    order = db.relationship('order', backref='order', lazy=True)
    item = db.relationship('item', backref='item', lazy=True)
    item_price = db.Column(db.Int(), nullable=False)
    amount = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'Item. {self.id}'
    

