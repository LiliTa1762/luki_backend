from config import db
from models.base_model import Basejson


class Property(Basejson, db.Model):
    """ Property table with all the info of the property """ 
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    startdate = db.Column(db.String(45), nullable=False)
    enddate = db.Column(db.String(45), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    country = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(512), nullable=False)
    building_name = db.Column(db.String(45), nullable=False)
    socialstratum = db.Column(db.Integer, nullable=False)
    price = db.Column(db.BigInteger, nullable=False)
    floor_number = db.Column(db.Integer, nullable=False)
    bedroom = db.Column(db.Integer, nullable=False)
    bathroom = db.Column(db.Integer, nullable=False)
    parkinglot = db.Column(db.Integer)
    mt2 = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024))

    property_of = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sector_of = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False)
    category_of = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
