from database.dao import achievementTypeDao
from flask import jsonify
from api import HttpStatus
from api.common.utils import sql_to_dict

class AchievementTypeHandler:
    
    def get_all_achievement_types():
        try:
            achievement_types = achievementTypeDao.get_all_achievement_types()
            result = []
            for achievement_type in achievement_types:
                dict_result = sql_to_dict(achievement_type)
                result.append(dict_result)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_achievement_type_by_id(id):
        try:
            achievement_type = achievementTypeDao.get_achievement_type_by_id(id)
            if (not achievement_type):
                return jsonify("Achievement type with ID: {} not found".format(id)), HttpStatus.NOT_FOUND.value 
            result = sql_to_dict(achievement_type)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason= "Server error", error = e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def create_achievement_type(json):
        try:
            new_achievement_type = achievementTypeDao.create_achievement_type(json)
            return jsonify("Achievement type with ID: {} has been created".format(new_achievement_type)), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def update_achievement_type(id, json):
        try:
            updated = achievementTypeDao.update_achievement_type(id, json)
            if (not updated):
                return jsonify("Achievement type with ID: {} not found".format(id)), HttpStatus.NOT_FOUND.value
            return jsonify("Achievement with ID: {} has been updated".format(id)), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_achievement_type(id):
        try:
            deleted = achievementTypeDao.delete_achievement_type(id)
            if (not deleted):
                return jsonify("Achievement type not found"), HttpStatus.NOT_FOUND.value
            return jsonify("Achievement with ID: {} has been deleted".format(id)), HttpStatus.OK.value
              
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value 



