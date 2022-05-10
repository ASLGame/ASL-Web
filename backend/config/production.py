import os

class ProductionConfig:
    host = os.environ.get('signy_db_host')
    name = os.environ.get('signy_db_name')
    password = os.environ.get('signy_db_password')
    database = os.environ.get('signy_db_database')
    secret_key = os.environ.get('signy_secret_key')
    secret_salt = os.environ.get('secret_salt')
    mail_username = os.environ.get('signy_mail_username')
    mail_password = os.environ.get('signy_mail_password')
    aws_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')