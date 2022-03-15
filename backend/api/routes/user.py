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
    
@app.route("/signy/accounts/signin", methods=['POST'])
def sign_in():
    if request.method == 'POST':
        return AccountHandler.sign_in(request.json)

@app.route("/signy/accounts/signup", methods=['POST'])
def sign_up():
    if request.method == 'POST':
        return AccountHandler.sign_up(request.json)

@app.route("/signy/confirm/<string:token>", methods=['GET'])
def confirm(token):
    if request.method == 'GET':
        return AccountHandler.confirm_email(token)