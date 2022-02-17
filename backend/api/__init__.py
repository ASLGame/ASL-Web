from flask import Flask
from flask_cors import CORS
# from flask_jwt_extended import JWTManager
from enum import IntEnum
from .dbconnection import DatabaseConnection as Database
from flask_jwt_extended import JWTManager

#AWS database credentials
# db = Database() #uncomment when DB set up

#App instance

app = Flask("Signy")
app.config['CORS_HEADER'] = 'Content-type'
app.config['SECRET_KEY'] = "signy"

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