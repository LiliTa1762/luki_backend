from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from os import getenv


application = app = Flask(__name__)

HBNB_MYSQL_USER = getenv('RDS_USERNAME')
HBNB_MYSQL_PWD = getenv('RDS_PASSWORD')
HBNB_MYSQL_HOST = getenv('RDS_HOSTNAME')
HBNB_MYSQL_PORT = getenv('RDS_PORT')
HBNB_MYSQL_DB = getenv('RDS_DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+mysqldb://{}:{}@{}:{}/{}'.format(
        HBNB_MYSQL_USER,
        HBNB_MYSQL_PWD,
        HBNB_MYSQL_HOST,
        HBNB_MYSQL_PORT,
        HBNB_MYSQL_DB
    )
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
Swagger(app)

db = SQLAlchemy(app)
