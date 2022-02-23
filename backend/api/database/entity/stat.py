from ... import db
from sqlalchemy import Column, Integer, Text

class Stat(db.Model):
    __tablename__ = 'Stats'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    type = Column(Text, nullable=False)