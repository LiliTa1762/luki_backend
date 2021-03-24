from config import db
from models.base_model import Basejson


class Category(Basejson, db.Model):
    """ Category table with info of type of property """ 
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    propertytype = db.Column(db.String(45), nullable=False)
