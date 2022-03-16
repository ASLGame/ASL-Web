import re
from flask import request
from api import app
from api.handler.game_handler import GameHandler

@app.route("/signy/game", methods=['GET', 'POST'])
def get_all_games_or_create():
    if request.method == 'GET':
        return GameHandler.get_all_games()
    elif request.method == 'POST':
        return GameHandler.create_game(request.json)

@app.route("/signy/game/<int:gid>", methods=['GET', 'DELETE', 'PUT'])
def get_game_by_id(gid):
    if request.method == 'GET':
        return GameHandler.get_game_by_id(gid)
    elif request.method == 'DELETE':
        return GameHandler.delete_game(gid)
    elif request.method == 'PUT':
        return GameHandler.update_game(gid, request.json)

@app.route("/signy/game/newest-game", methods=['GET'])
def get_newest_game():
    if request.method == 'GET':
        return GameHandler.get_newest_game()

@app.route("/signy/game/featured-games", methods=['GET'])
def get_featured_games():
    if request.method == 'GET':
        return GameHandler.get_featured_games()