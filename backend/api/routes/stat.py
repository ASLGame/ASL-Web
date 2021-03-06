from flask import request
from api import app
from api.handler.stat import StatHandler

@app.route("/signy/stat", methods=['GET', 'POST'])
def get_all_stats_or_create():
    if request.method == 'GET':
        return StatHandler.get_all_stats()
    else:
        return StatHandler.create_stat(request.json)

@app.route("/signy/stat/<string:type>")
@app.route("/signy/stat/<int:id>", methods= ['GET', 'PUT', 'DELETE'])
def stat_by_id(id=None, type=None):
    if request.method == 'GET':
        if(id):
            return StatHandler.get_stat_by_id(id)
        elif(type):
            return StatHandler.get_stat_by_type(type)
    elif request.method == 'PUT':
        return StatHandler.update_stat(id, request.json)
    else:
        return StatHandler.delete_stat(id)
