from api import db
from sqlalchemy import Column, Integer, ForeignKey, Boolean, text, Date, DateTime
from sqlalchemy.orm import relationship
class AccountAchievements(db.Model):
    __tablename__ = 'Account_Achievements'

    id = Column(Integer, primary_key=True)
    account_id = Column(ForeignKey('Account.id', ondelete='CASCADE'), nullable=False)
    achievement_id = Column(ForeignKey('Achievement.id', ondelete='CASCADE'), nullable=False)
    has_achieved = Column(Boolean, nullable=False, server_default=text("false"))
    date_achieved = Column(Date)
    date_created = Column(DateTime(True), nullable=False)
    date_updated = Column(DateTime(True), nullable=False)
    
    account = relationship('Account')
    achievement = relationship('Achievement')