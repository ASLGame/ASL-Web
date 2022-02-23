from ... import db
from sqlalchemy import Column, DateTime, Integer, ForeignKey, text
from sqlalchemy.orm import relationship

class Score(db.Model):
    __tablename__ = 'Score'

    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)
    date_achieved = Column(DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    account_id = Column(ForeignKey('Account.id', ondelete='CASCADE'), nullable=False)
    game_id = Column(ForeignKey('Game.id', ondelete='CASCADE'), nullable=False)

    account = relationship('Account')
    game = relationship('Game')