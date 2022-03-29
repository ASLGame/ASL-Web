from api import db
from sqlalchemy import Column, DateTime, Integer, Text, text, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

class Achievement(db.Model):
    __tablename__ = 'Achievement'

    id = Column(Integer, primary_key=True)
    account_stats_id = Column(ForeignKey('Account_Stats.id', ondelete='CASCADE'), nullable=False)
    game_id = Column(ForeignKey('Game.id', ondelete='CASCADE'), nullable=False)
    name = Column(Text, nullable=False)
    type = Column(Text, nullable=False)
    task = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    date_created = Column(DateTime(True), nullable=False)

    account_stats = relationship('AccountStat')
    game = relationship('Game')