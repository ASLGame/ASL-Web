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

@app.route("/signy/accounts/edit/profile/<int:uid>", methods=['PUT'])
def edit_profile(uid):
    if request.method == 'PUT':
        return AccountHandler.edit_profile(uid, request.json)

@app.route("/signy/accounts/edit/password/<int:uid>", methods=['PUT'])
def change_password(uid):
    if request.method == 'PUT':
        return AccountHandler.change_password(uid, request.json)

@app.route("/signy/accounts/upload/profile/picture/<int:uid>/<string:username>", methods=['POST'])
def upload_profile_picture(uid, username):
    if request.method == 'POST':
        image = request.files.get('userpic')
        return AccountHandler.upload_profile_picture(image, uid, username)