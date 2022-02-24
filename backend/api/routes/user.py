from api import app
from database.dao import AccountDao
@app.route("/hello")
def hello_world():
    print(AccountDao.getAllAccounts())
    return "Hello World"