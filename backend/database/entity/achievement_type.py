from api import db
from sqlalchemy import Column, Integer, Text

class AchievementType(db.Model):
    __tablename__ = 'Achievement_Type'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text)
    type = Column(Text, nullable=False)