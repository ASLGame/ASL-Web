from database.entity import game
from database.dao import gameDao
from flask import jsonify
from api import HttpStatus

class GameHandler:

    def get_all_games():
        try:
            game_dao = gameDao.get_all_games()
            return jsonify(game_dao), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def create_game(json):
        try:
            game_dao = gameDao.create_game(json)
            if game_dao:
                return jsonify(game_dao), HttpStatus.CREATED.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_game_by_id(gid):
        pass

    def delete_game(gid):
        pass

    def update_game(gid, json):
        pass