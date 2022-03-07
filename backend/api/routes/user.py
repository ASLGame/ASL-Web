from api import app
from api.handler.account_handler import AccountHandler
from flask import request

@app.route("/hello")
def hello_world():
    return "Hello World"

@app.route("/signy/accounts", methods=['GET', 'POST'])
def get_all_accounts_or_create():
    if request.method == 'GET':
        return AccountHandler.get_all_accounts()
    elif request.method == 'POST':
        return AccountHandler.create_account(request.json)

@app.route("/signy/accounts/<int:uid>", methods=['GET', 'PUT', 'DELETE'])
def get_update_delete_account_by_id(uid):
    if request.method == 'GET':
        return AccountHandler.get_account_id(uid)
    elif request.method == 'PUT':
        return AccountHandler.update_account(uid, request.json)
    elif request.method == 'DELETE':
        return AccountHandler.delete_account(uid)
    

