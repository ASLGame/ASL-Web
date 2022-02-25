from api import db
from sqlalchemy import Column, DateTime, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

class TimeBasedAchievement(db.Model):
    __tablename__ = 'Time_Based_Achievement'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    task = Column(Integer, nullable=False)
    achievement_type_id = Column(ForeignKey('Achievement_Type.id'), nullable=False)
    stats_id = Column(ForeignKey('Stats.id'), nullable=False)
    start_date = Column(DateTime(True), nullable=False)
    end_date = Column(DateTime(True), nullable=False)

    achievement_type = relationship('AchievementType')
    stats = relationship('Stat')