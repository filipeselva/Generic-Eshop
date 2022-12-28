from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #we doesn't use the Flask-SQLAlchemy event system.
db = SQLAlchemy(app)
ma = Marshmallow(app) # Needs to inicialized after SQLAlchemy.

app.app_context().push()

# Needs to be after the app initialization.
from database import routes