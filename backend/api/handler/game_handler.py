from database.dao import gameDao
from flask import jsonify
from api import HttpStatus
from api.common.utils import sql_to_dict

class GameHandler:

    def get_all_games():
        try:
            game_dao = gameDao.get_all_games()
            result = []
            for g in game_dao:
                g = sql_to_dict(g)
                result.append(g)
            return jsonify(result), HttpStatus.OK.value
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
        try:
            game_dao = gameDao.get_game_by_id(gid)
            game_dao = sql_to_dict(game_dao)
            if game_dao:
                return jsonify(game_dao), HttpStatus.OK.value
            else:
                return jsonify("Game with ID: {} not found".format(gid)), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_game(gid):
        try:
            game_dao_deleted = gameDao.delete_game(gid)
            if game_dao_deleted:
                return jsonify("Game deleted successfully"), HttpStatus.OK.value
            else:
                return jsonify("Game not found"), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def update_game(gid, json):
        try:
            game_dao_updated = gameDao.update_game(gid, json)
            if game_dao_updated:
                return jsonify(game_dao_updated), HttpStatus.OK.value
            else:
                return jsonify("Game not found"), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value