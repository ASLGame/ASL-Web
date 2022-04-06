import re
from flask import request
from api import app
from api.handler.game_asset_handler import GameAssetHandler

@app.route("/signy/assets", methods=['GET', 'POST'])
def get_all_assets_or_create():
    if request.method == 'GET':
        return GameAssetHandler.get_all_assets()
    elif request.method == 'POST':
        return GameAssetHandler.create_game_asset(request.json)

@app.route('/signy/assets/<int:aid>', methods=['GET', 'PUT', 'DELETE'])
def get_delete_update_asset(aid):
    if request.method == 'GET':
        return GameAssetHandler.get_asset_id(aid)
    elif request.method == 'PUT':
        return GameAssetHandler.update_game_asset(aid, request.json)
    elif request.method == 'DELETE':
        return GameAssetHandler.delete_asset_id(aid)