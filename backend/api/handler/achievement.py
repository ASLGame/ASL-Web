from api.handler.account_achievements import AccountAchievementsHandler
from database.dao import achievementDao
from flask import jsonify
from api import HttpStatus
from api.common.utils import sql_to_dict

class AchievementHandler:

    def get_all_achievements():
        try:
            achievement = achievementDao.get_all_achievements()
            result = []
            for ach in achievement:
                dictStat = sql_to_dict(ach)
                result.append(dictStat)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_achievement_id(id):
        try:
            achievement = achievementDao.get_achievement_id(id)
            if not achievement:
                return jsonify("Achievement with ID: {} does not exist.".format(id)), HttpStatus.NOT_FOUND.value
            result = sql_to_dict(achievement)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def create_achievement(json):
        try: 
            achievement = achievementDao.create_achievement(json)
            if(achievement): #Create account achievements
                res = AccountAchievementsHandler.add_new_account_achievements(achievement)
                if (res[1] == 200):
                    return jsonify("Achievement created with ID {}".format(achievement)), HttpStatus.OK.value
                else:
                    AchievementHandler.delete_achievement(achievement)
                    return jsonify(reason="Could not update all account achievements because {}".format(res[0].get_json())), HttpStatus.BAD_REQUEST.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def update_achievement(id, json):
        try:
            achievement = achievementDao.update_achievement(id, json)
            if not achievement:
                return jsonify("Achievement not found."), HttpStatus.NOT_FOUND.value
            return jsonify("Achievement updated successfully"), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_achievement(id):
        try: 
            achievement = achievementDao.delete_achievement(id)
            if not achievement:
                return jsonify("Achievement not found."), HttpStatus.NOT_FOUND.value
            return jsonify("Achievement deleted."), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_game_achievements(gid):
        try: 
            game_achievements = achievementDao.get_game_achievements(gid)
            if not game_achievements:
                return jsonify("Game achievements not found."), HttpStatus.NOT_FOUND.value
            result = []
            for ach in game_achievements:
                result.append(sql_to_dict(ach))
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value