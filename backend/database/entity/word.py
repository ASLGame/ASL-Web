from api import db
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

class Word(db.Model):
    __tablename__ = 'Word'

    id = Column(Integer, primary_key=True)
    bank_id = Column(ForeignKey('Bank.id', ondelete='CASCADE'), nullable=False)
    word = Column(Text, nullable=False, unique=True)
    difficulty = Column(Integer, nullable=False)

    bank = relationship('Bank')