from ... import db
from sqlalchemy import Column, Integer, Text

class Bank(db.Model):
    __tablename__ = 'Bank'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)