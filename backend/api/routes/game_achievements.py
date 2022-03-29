import re
from flask import request
from api import app
from api.handler.game_achievement import Game_Achievement_Handler

# @app.route("/signy/game_achievements", methods=['GET', 'POST'])
# def get_all_achievements_or_create():
#     if request.method == 'GET':
#         return Game_Achievement_Handler.get_all_game_achievements()
#     elif request.method == 'POST':
#         return Game_Achievement_Handler.create_game_achievement(request.json)

@app.route("/signy/game_achievements/<int:gaid>", methods=['GET', 'PUT', 'DELETE'])
def get_update_delete_achievement(gaid):
    if request.method == 'GET':
        return Game_Achievement_Handler.get_game_achievement_id(gaid)
    elif request.method == 'PUT':
        return Game_Achievement_Handler.update_game_achievement(gaid, request.json)
    elif request.method == 'DELETE':
        return Game_Achievement_Handler.delete_game_achievement(gaid, request.json)