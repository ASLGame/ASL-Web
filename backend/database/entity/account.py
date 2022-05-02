from api import db
from sqlalchemy import Column, DateTime, Integer, Text, text, Boolean, Date

class Account(db.Model):
    __tablename__ = 'Account'

    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False, unique=True)
    email = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    DOB = Column(Date, nullable=False)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    date_created = Column(DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    date_updated = Column(DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    role = Column(Text, nullable=False)
    email_confirmed = Column(Boolean, nullable=False, default=False)
    profile_picture_path = Column(Text)