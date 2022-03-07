from api import db
from sqlalchemy import Column, DateTime, Integer, Text, text

class Account(db.Model):
    __tablename__ = 'Account'

    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False, unique=True)
    email = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    DOB = Column(DateTime(True), nullable=False)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    date_created = Column(DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    date_updated = Column(DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    role = Column(Text, nullable=False)