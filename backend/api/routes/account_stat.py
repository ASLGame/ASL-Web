from flask import request
from api import app
from api.handler.account_stat import AccountStatHandler

@app.route("/signy/account-stat", methods=['GET', 'POST'])
def get_all_account_stats_or_create():
    if request.method == 'GET':
        return AccountStatHandler.get_all_account_stats()
    else:
        return AccountStatHandler.create_account_stat(request.json)

@app.route("/signy/account-stat/<int:id>", methods= ['GET', 'PUT', 'DELETE'])
def account_stat_by_id(id):
    if request.method == 'GET':
        return AccountStatHandler.get_account_stat_by_id(id)
    elif request.method == 'PUT':
        return AccountStatHandler.update_account_stat(id, request.json)
    else:
        return AccountStatHandler.delete_account_stat(id)

@app.route("/signy/account-stat/<int:aid>/<int:sid>", methods=['PUT', 'GET'])
def account_stat_get_update(aid, sid):
    if request.method == 'PUT':
        return AccountStatHandler.account_stat_update(aid, sid, request.json)