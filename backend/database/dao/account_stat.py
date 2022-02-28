from api import db
from ..entity import account_stat
from datetime import datetime

class AccountStatDao:

    @staticmethod
    def get_all_account_stats():
        return account_stat.query.all()
    
    @staticmethod
    def get_account_stat_by_id(id):
        return account_stat.query.get(id)

    @staticmethod
    def create_account_stat(json):
        new_account_stat = account_stat(account_id = json['account_id'], value = json['value'], stats_id = json["stats_id"])
        db.session.add(new_account_stat)
        db.session.commit()

        return new_account_stat.id

    @staticmethod
    def update_account_stat(id, json):
        update_account_stat = db.session.query(account_stat).where(account_stat.id == id).update({ "value": json['value'], "date_updated": datetime.utcnow()})
        db.session.commit()
        return update_account_stat

    @staticmethod
    def update_achieved_account_stat(id, json):
        update_account_stat = db.session.query(account_stat).where(account_stat.id == id).update({ "value": json['value'], "has_achieved": json['has_achieved'], "date_achieved": datetime.utcnow(), "date_updated": datetime.utcnow()})
        db.session.commit()
        return update_account_stat
    
    @staticmethod
    def delete_account_stat(id):
        delete_account = db.session.query(account_stat).where(account_stat.id == id).delete()
        db.session.commit()
        return delete_account

    