from database.dao import gameachievementsDAO
from flask import jsonify
from api import HttpStatus
from api.common.utils import sql_to_dict

class Game_achievement_Handler:

    def get_all_game_achievements():
        try:
            achievements = gameachievementsDAO.get_all_game_achievements()
            result = []
            for a in achievements:
                a = sql_to_dict(a)
                result.append(a)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_game_achievement_id(gaid):
        try:
            achievement = gameachievementsDAO.get_game_achievement_id(gaid)
            achievement = sql_to_dict(achievement)
            if achievement:
                return jsonify(achievement), HttpStatus.OK.value
            else:
                return jsonify("Game Achievement with ID: {} not found".format(gaid)), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_game_achievement_stats_id(stid):
        try:
            achievement = gameachievementsDAO.get_game_achievement_stats_id(stid)
            achievement = sql_to_dict(achievement)
            if achievement:
                return jsonify(achievement), HttpStatus.OK.value
            else:
                return jsonify("Game Achievement with Stats ID: {} not found".format(stid)), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_game_achievement_game_id(gid):
        try:
            achievement = gameachievementsDAO.get_game_achievement_game_id(gid)
            achievement = sql_to_dict(achievement)
            if achievement:
                return jsonify(achievement), HttpStatus.OK.value
            else:
                return jsonify("Game Achievement with Game ID: {} not found".format(gid)), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value
    
    def get_game_achievement_achievement_id(aid):
        try:
            achievement = gameachievementsDAO.get_game_achievement_achievement_id(aid)
            achievement = sql_to_dict(achievement)
            if achievement:
                return jsonify(achievement), HttpStatus.OK.value
            else:
                return jsonify("Game Achievement with Achievement ID: {} not found".format(aid)), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def create_game_achievement(json):
        try:
            achievement = gameachievementsDAO.create_game_achievement(json)
            if achievement:
                return jsonify(achievement), HttpStatus.CREATED.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def update_game_achievement(gaid, json):
        try:
            achievement = gameachievementsDAO.update_game_achievement(gaid, json)
            if achievement:
                return jsonify(achievement), HttpStatus.OK.value
            else:
                return jsonify("Game Achievement not found"), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_game_achievement(gaid):
        try:
            achievement = gameachievementsDAO.delete_game(gaid)
            if achievement:
                return jsonify("Game Achievement deleted successfully"), HttpStatus.OK.value
            else:
                return jsonify("Game Achievement not found"), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value
