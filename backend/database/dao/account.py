from ..entity import account
from api import db
from passlib.hash import pbkdf2_sha256 as sha256

class AccountDao: 
    
    @staticmethod  # Gets all accounts
    def getAllAccounts():
        return account.query.all()

    @staticmethod  # Creates new account
    def create_account(json):
        hashed_password = sha256.hash(json['password'])
        new_account = account(username=json['username'], email=json['email'], password=hashed_password, DOB=json['DOB'], first_name=json['first_name'], last_name=json['last_name'], 
                        role=json['role'])
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
        return db.session.query(account).filter(account.username == uname).first()

    @staticmethod  # Gets all accounts with the same DOB
    def get_account_DOB(dob):
        return db.session.query(account).filter(account.DOB == dob).first()

    @staticmethod  # Gets all accounts with the same DOB
    def get_account_email(email):
        account_email = db.session.query(account).filter(account.email == email).first()
        # db.session.commit()
        return account_email

    @staticmethod  # Updates account; doesn't update username nor date created
    def update_account(uid, json):
        account_updated = db.session.query(account).where(account.id == uid).update({"password": json['password'], "email":json['email'], "DOB": json['DOB'], "first_name":json['first_name'], "last_name":json['last_name'],
                                                                                    "date_updated": json['date_updated'], "role":json['role']})
        db.session.commit()
        return account_updated

    @staticmethod  # Updates account; doesn't update username nor date created
    def confirm_account(uid):
        account_updated = db.session.query(account).where(account.id == uid).update({"email_confirmed": True})
        db.session.commit()
        return account_updated

    @staticmethod  # Returns all accounts with the same first name
    def get_account_fn(fname):
        return db.session.query(account).filter(account.first_name == fname).first()

    @staticmethod  # Returns all accounts with the same last name
    def get_account_ln(lname):
        return db.session.query(account).filter(account.last_name == lname).first()

        