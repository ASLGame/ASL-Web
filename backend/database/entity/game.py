from api import db
from sqlalchemy import Column, DateTime, Integer, Text, text, ForeignKey
from sqlalchemy.orm import relationship
from .game_asset import GameAsset

class Game(db.Model):

    __tablename__ = 'Game'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    description = Column(Text, nullable=False)
    rules = Column(Text, nullable=False)
    type = Column(Text, nullable=False)
    date_created = Column(DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    bank_id = Column(ForeignKey('Bank.id'), nullable=False)

    bank = relationship('Bank')
    gameAssets = relationship(GameAsset, back_populates='game')