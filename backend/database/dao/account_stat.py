from webbrowser import get
from api import db
from database.dao.account import AccountDao
from ..entity import account_stat
from datetime import datetime
from .stat import StatDao
from api.common.utils import sql_to_dict

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
        update_account_stat = db.session.query(account_stat).where(account_stat.id == id).update({ "value": json['value'], "date_updated": datetime.utcnow()})
        db.session.commit()
        return update_account_stat
    
    @staticmethod
    def delete_account_stat(id):
        delete_account = db.session.query(account_stat).where(account_stat.id == id).delete()
        db.session.commit()
        return delete_account

    @staticmethod
    def account_stats_initialize(id):
        stats = StatDao.get_all_stats()
        successful = []
        for stat in stats:
            info = {'account_id': id, 'stats_id': stat.id, 'value': 0}
            res = AccountStatDao.create_account_stat(info)
            successful.append(res)
        if (len(successful) == len(stats)):
            return True
        return False
    
    # If we create a new stat, existing accounts must be updated with this new account_stat
    @staticmethod
    def add_new_account_stat(sid):
        accounts = AccountDao.getAllAccounts()
        successful = []
        for acc in accounts:
            info = {'account_id': acc.id, 'stats_id': sid, 'value': 0}
            res = AccountStatDao.create_account_stat(info)
            successful.append(res)
        if (len(successful) == len(accounts)):
            return True
        return False

    # Get account stat by account id and stat id
    @staticmethod
    def get_account_stat_by_acc_id_stat_id(aid, sid):
        get_account_stat = db.session.query(account_stat).filter(account_stat.account_id == aid, account_stat.stats_id == sid).first()
        return get_account_stat

    # This update method will be used with the frontend application to update an account stats value. Only for non-time values.
    @staticmethod
    def account_stat_update(aid, sid, json):
        get_account_stat = AccountStatDao.get_account_stat_by_acc_id_stat_id(aid, sid)
        return AccountStatDao.update_account_stat(get_account_stat.id, {"value": get_account_stat.value + json})