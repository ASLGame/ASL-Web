from ..entity import account

class AccountDao: 
    
    @staticmethod
    def getAllAccounts():
        return account.query.all()