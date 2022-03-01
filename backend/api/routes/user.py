from api import app
from api.handler.account_handler import AccountHandler

@app.route("/hello")
def hello_world():
    return "Hello World"