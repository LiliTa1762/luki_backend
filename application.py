from blueprints.base_routes import base_page
from config import db, application
from models.user import User
from models.category import Category
from models.sector import Sector
from models.property import Property


application.register_blueprint(base_page)

db.create_all()
