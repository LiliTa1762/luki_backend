from config import db
from models.base_model import Basejson


class Sector(Basejson, db.Model):
    """ Sector table with info of the neighborhood in Barranquilla """ 
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), nullable=False, unique=True)
