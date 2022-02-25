from flask import Flask
from flask_cors import CORS
from enum import IntEnum
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from config import load_config

#App instance
app = Flask("Signy")
config = load_config()
app.config['CORS_HEADER'] = 'Content-type'
app.config['SECRET_KEY'] = config.secret_key

# Database connection.
DB_URI = f'postgresql://{config.name}:{config.password}@{config.host}:5432/{config.database}'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

jwt = JWTManager(app)

CORS(app, support_credentials=True)

class HttpStatus(IntEnum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    UNAUTHORIZED = 401

# import routes
from .routes import *