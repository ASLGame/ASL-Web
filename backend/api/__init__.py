from flask import Flask
from flask_mail import Mail
from flask_cors import CORS
from enum import IntEnum
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from config import load_config
import boto3

#App instance
app = Flask("Signy")
config = load_config()
print(config.host)
app.config['CORS_HEADER'] = 'Content-type'
app.config['SECRET_KEY'] = config.secret_key
app.config['SECRET_SALT'] = config.secret_salt
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = config.mail_username
app.config['MAIL_PASSWORD'] = config.mail_password

# Database connection.
DB_URI = f'postgresql://{config.name}:{config.password}@{config.host}:5432/{config.database}'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

jwt = JWTManager(app)
mail = Mail(app)
CORS(app, support_credentials=True)

# AWS BOTO3 Using Amazon S3 instance
s3 = boto3.client('s3')


class HttpStatus(IntEnum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    UNAUTHORIZED = 401

# import routes
from .routes import *