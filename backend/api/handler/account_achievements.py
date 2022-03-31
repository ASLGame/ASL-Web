from database.dao import accountAchievementsDao
from flask import jsonify
from api import HttpStatus
from api.common.utils import sql_to_dict

class AccountAchievementsHandler:

    def get_all_account_achievements():
        try:
            account_achievement = accountAchievementsDao.get_all_account_achievements()
            result = []
            for stat in account_achievement:
                dictStat = sql_to_dict(stat)
                result.append(dictStat)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_account_achievements_id(id):
        try:
            account_achievement = accountAchievementsDao.get_account_achievements_id(id)
            if not account_achievement:
                return jsonify("Account Achievement with ID: {} does not exist.".format(id)), HttpStatus.NOT_FOUND.value
            result = sql_to_dict(account_achievement)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def create_account_achievements(json):
        try: 
            account_achievement = accountAchievementsDao.create_account_achievements(json)
            return jsonify("Account Achievement created with ID {}".format(account_achievement)), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def update_account_achievements(id, json):
        try:
            # if (json.get('has_achieved')):
                
            #     account_stat = accountAchievementsDao.update_achieved_account_stat(id, json)
            # else:
            account_achievement = accountAchievementsDao.update_account_achievements(id, json)
            if not account_achievement:
                return jsonify("Account Achievement not found."), HttpStatus.NOT_FOUND.value
            return jsonify("Account Achievement updated successfully"), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_account_achievements(id):
        try: 
            account_achievement = accountAchievementsDao.delete_account_achievements(id)
            if not account_achievement:
                return jsonify("Account Achievement not found."), HttpStatus.NOT_FOUND.value
            return jsonify("Account Achievement deleted."), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_user_account_achievement(id):
        try:
            account_achievement = accountAchievementsDao.get_user_account_achievement(id)
            result = []
            for a in account_achievement:
                result.append(dict(a))
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value
