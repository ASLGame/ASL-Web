from flask import request
from api import app
from api.handler.bank_handler import BankHandler

@app.route("/signy/bank", methods=['GET', 'POST'])
def get_all_banks_or_create():
    if request.method == 'GET':
        return BankHandler.get_all_banks()
    elif request.method == 'POST':
        return BankHandler.create_bank(request.json)

@app.route("/signy/bank/<int:bid>", methods=['GET', 'DELETE', 'PUT'])
def get_bank_by_id(bid):
    if request.method == 'GET':
        return BankHandler.get_bank_by_id(bid)
    elif request.method == 'DELETE':
        return BankHandler.delete_bank(bid)
    elif request.method == 'PUT':
        return BankHandler.update_bank(bid, request.json)