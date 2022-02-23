import os

class ProductionConfig:
    host = os.environ.get('signy_db_host')
    name = os.environ.get('signy_db_name')
    password = os.environ.get('signy_db_password')
    database = os.environ.get('signy_db_database')
    secret_key = os.environ.get('signy_secret_key')