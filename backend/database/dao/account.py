from ..entity import account
from api import db

class AccountDao: 
    
    @staticmethod
    def getAllAccounts():
        return account.query.all()

    @staticmethod
    def create_account(json):
        new_account = account(username=json['username'], password=json['password'], DOB=json['DOB'], first_name=json['first_name'], last_name=json['last_name'], 
                                date_created=json['date_created'], date_updated=json['date_created'], role=json['role'])
        db.session.add(new_account)
        db.session.commit()