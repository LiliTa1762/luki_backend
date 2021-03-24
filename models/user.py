from config import db
from models.base_model import Basejson


class User(Basejson, db.Model):
    """ User table for the info of the users """ 
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.Integer, nullable=False, unique=False)
    password = db.Column(db.String(8), nullable=False)
