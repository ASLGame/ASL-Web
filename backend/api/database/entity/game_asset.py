from ... import db
from sqlalchemy import Column, DateTime, Integer, Text, text, ForeignKey
from sqlalchemy.orm import relationship

class GameAsset(db.Model):
    __tablename__ = 'Game_Asset'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text)
    type = Column(Text, nullable=False)
    path = Column(Text, nullable=False)
    date_created = Column(DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    date_updated = Column(DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    game_id = Column(ForeignKey('Game.id', ondelete='CASCADE'), nullable=False)

    game = relationship('Game')
