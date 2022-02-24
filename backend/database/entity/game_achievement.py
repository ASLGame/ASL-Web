from api import db
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

class GameAchievement(db.Model):
    __tablename__ = 'Game_Achievement'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    descrition = Column(Text, nullable=False)
    task = Column(Integer, nullable=False)
    achievement_type_id = Column(ForeignKey('Achievement_Type.id'), nullable=False)
    stats_id = Column(ForeignKey('Stats.id'), nullable=False)
    game_id = Column(ForeignKey('Game.id', ondelete='CASCADE'), nullable=False)

    achievement_type = relationship('AchievementType')
    game = relationship('Game')
    stats = relationship('Stat')