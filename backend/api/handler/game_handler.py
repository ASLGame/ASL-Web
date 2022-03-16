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
                assets = g.gameAssets
                g = sql_to_dict(g)
                g['gameAssets'] = []
                for ga in assets:
                    g['gameAssets'].append(sql_to_dict(ga))
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
            assets = game_dao.gameAssets
            game_dao = sql_to_dict(game_dao)
            game_dao['gameAssets'] = []
            for ga in assets:
                game_dao['gameAssets'].append(sql_to_dict(ga))
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

    def get_newest_game():
        try:
            newest_game = gameDao.newest_game()
            assets = newest_game.gameAssets
            newest_game = sql_to_dict(newest_game)
            newest_game['gameAssets'] = []
            for ga in assets:
                newest_game['gameAssets'].append(sql_to_dict(ga))
            if newest_game:
                return jsonify(newest_game), HttpStatus.OK.value
            return jsonify("There are no games."), HttpStatus.BAD_REQUEST.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_featured_games():
        try:
            featured_games = gameDao.featured_games()
            result = []
            for g in featured_games:
                assets = g.gameAssets
                g = sql_to_dict(g)
                g['gameAssets'] = []
                for ga in assets:
                    g['gameAssets'].append(sql_to_dict(ga))
                result.append(g)
            if result:
                return jsonify(result), HttpStatus.OK.value
            return jsonify("There are no games."), HttpStatus.BAD_REQUEST.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value
            