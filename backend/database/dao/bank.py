from ..entity import bank
from api import db

class BankDao: 
    
    @staticmethod
    def get_all_banks():
        return bank.query.all()
    
    @staticmethod
    def create_bank(json):
        new_bank = bank(name=json['name'], description=json['description'])
        db.session.add(new_bank)
        db.session.commit()

        return new_bank.id
    
    @staticmethod
    def get_bank_by_id(bid):
        return bank.query.get(bid)

    @staticmethod
    def delete_bank(bid):
        bank_deleted = db.session.query(bank).where(bank.id==bid).delete()
        db.session.commit()
        return bank_deleted

    @staticmethod
    def update_bank(bid, json):
        bank_updated = db.session.query(bank).where(bank.id==bid).update({"name": json['name'], "description":json['description']})
        db.session.commit()
        return bank_updated