from ... import db
from sqlalchemy import Column, DateTime, Integer, text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class AccountStat(db.Model):
    __tablename__ = 'Account_Stats'

    id = Column(Integer, primary_key=True)
    account_id = Column(ForeignKey('Account.id', ondelete='CASCADE'), nullable=False)
    value = Column(Integer, nullable=False)
    has_achieved = Column(Boolean, nullable=False, server_default=text("false"))
    date_achieved = Column(DateTime(True))
    date_created = Column(DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    date_updated = Column(DateTime(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    stats_id = Column(ForeignKey('Stats.id', ondelete='CASCADE'))

    account = relationship('Account')
    stats = relationship('Stat')