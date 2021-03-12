from flask import Blueprint
from flask_cors import CORS
from flasgger.utils import swag_from
from models.user import User
from models.property import Property
from flask import jsonify, make_response, abort, request
from flask_sqlalchemy import SQLAlchemy
from config import db


base_page = Blueprint('base_page', __name__, url_prefix='/api/v1.0')

CORS(base_page)


@base_page.route('/', strict_slashes=False, methods=['GET'])
@swag_from('../flasgger/get_routes.yml')
def starting_url():
    """ Return the status of the API to check that it works """
    return jsonify({"status": "OK"}), 200


@base_page.route('/landlord/<id>', strict_slashes=False, methods=['GET'])
@swag_from('../flasgger/get_landlord_id_users.yml')
def landlord_id_users(id):
    """ Returns landlord user by ID """
    user_list = User.query.filter(User.id == id).first()
    if user_list is None:
        return jsonify({"reason": "non-existing ID", "not found": "404"}), 404
    return make_response(jsonify(user_list.to_dict())), 200


@base_page.route('/landlord', strict_slashes=False, methods=['POST'])
@swag_from('../flasgger/post_create_landlord.yml')
def create_landlord():
    """ Insert a landlord user in DB """
    body_json: dict = request.get_json()
    name: str = body_json.get("name")
    lastname: str = body_json.get("lastname")
    email: str = body_json.get("email")
    phone: int = body_json.get("phone")
    password: str = body_json.get("password")

    new_user: User = User(name=name, lastname=lastname, email=email, phone=phone, password=password)

    db.session.add(new_user)
    db.session.commit()

    user = new_user.query.get(new_user.id)

    return make_response(jsonify({'users': user.to_dict()})), 200


@base_page.route('/rents/', strict_slashes=False, methods=['GET'])
@swag_from('../flasgger/get_apart_for_rent.yml')
def apart_for_rent():
    """ Returns all apartments for rent """
    apart_list = Property.query.all()
    all_apart = []
    for place in apart_list:
        apartment = place.__dict__
        apartment.pop('_sa_instance_state')
        all_apart.append(apartment)
    if apart_list is None:
        return jsonify({"reason:": "non-available apartment", "not found": "404"}), 404
    return make_response(jsonify({'apartment': all_apart})), 200


@base_page.route('/rents', strict_slashes=False, methods=['POST'])
@swag_from('../flasgger/post_create_apartment.yml')
def create_apartment():
    """ Add a new apartment for rent """
    apartment: dict = request.get_json()
    startdate: str = apartment.get('startdate')
    enddate: str = apartment.get('enddate')
    latitude: float = apartment.get('latitude')
    longitude: float = apartment.get('longitude')
    country: str = apartment.get('country')
    state: str = apartment.get('state')
    city: str = apartment.get('city')
    address: str = apartment.get('address')
    building_name: str = apartment.get('building_name')
    socialstratum: int = apartment.get('socialstratum')
    price: int = apartment.get('price')
    floor_number: int = apartment.get('floor_number')
    bedroom: int = apartment.get('bedroom')
    bathroom: int = apartment.get('bathroom')
    parkinglot: int = apartment.get('parkinglot')
    mt2: int = apartment.get('mt2')
    description: str = apartment.get('description')
    property_of: int = apartment.get('property_of')
    sector_of: int = apartment.get('sector_of')
    category_of: int = apartment.get('category_of')

    new_apartment: Property = Property(startdate=startdate, enddate=enddate, latitude=latitude, longitude=longitude, country=country,
                                       state=state, city=city, address=address, building_name=building_name, socialstratum=socialstratum, price=price, 
                                       floor_number=floor_number, bedroom=bedroom, bathroom=bathroom, parkinglot=parkinglot, mt2=mt2, description=description, 
                                       property_of=property_of, sector_of=sector_of, category_of=category_of)

    db.session.add(new_apartment)
    db.session.commit()

    apartment = new_apartment.query.get(new_apartment.id)

    return make_response(jsonify({'new apartment': apartment.to_dict()})), 200
