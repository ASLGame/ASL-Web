from ..entity import account
from api import db

class AccountDao: 
    
    @staticmethod  # Gets all accounts
    def getAllAccounts():
        return account.query.all()

    @staticmethod  # Creates new account
    def create_account(json):
        new_account = account(username=json['username'], email=json['email'], password=json['password'], DOB=json['DOB'], first_name=json['first_name'], last_name=json['last_name'], 
                                date_created=json['date_created'], date_updated=json['date_created'], role=json['role'])
        db.session.add(new_account)
        db.session.commit()
        return new_account.id

    @staticmethod  # Deletes account based on id
    def delete_account_id(uid):
        account_deleted = db.session.query(account).where(account.id == uid).delete()
        db.session.commit()
        return account_deleted

    @staticmethod # Gets account based on its ID
    def get_account_id(uid):
        return account.query.get(uid)

    @staticmethod  # Gets account based on username
    def get_account_username(uname):
        return db.session.query(account).filter(account.username == uname)

    @staticmethod  # Gets all accounts with the same DOB
    def get_account_DOB(dob):
        return db.session.query(account).filter(account.DOB == dob)

    @staticmethod  # Updates account; doesn't update username nor date created
    def update_account(uid, json):
        account_updated = db.session.query(account).where(account.id == uid).update({"password": json['password'], "email":json['email'], "DOB": json['DOB'], "first_name":json['first_name'], "last_name":json['last_name'],
                                                                                    "date_updated": json['date_updated'], "role":json['role']})
        db.session.commit()
        return account_updated

    @staticmethod  # Returns all accounts with the same first name
    def get_account_fn(fname):
        return db.session.query(account).filter(account.first_name == fname)

    @staticmethod  # Returns all accounts with the same last name
    def get_account_ln(lname):
        return db.session.query(account).filter(account.last_name == lname)

        