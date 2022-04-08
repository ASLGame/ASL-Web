from api.handler.account_stat import AccountStatHandler
from database.dao import statDao
from flask import jsonify
from api import HttpStatus
from api.common.utils import sql_to_dict

class StatHandler:

    def get_all_stats():
        try: 
            stats = statDao.get_all_stats()
            result = []
            for stat in stats:
                dictStat = sql_to_dict(stat)
                result.append(dictStat)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value
    
    def get_stat_by_id(id):
        try: 
            stat = statDao.get_stat_by_id(id)
            if not stat:
                return jsonify("Stat with ID: {} does not exist.".format(id)), HttpStatus.NOT_FOUND.value
            result = sql_to_dict(stat)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def create_stat(json):
        try: 
            stat = statDao.create_stat(json)
            if(stat):
                res = AccountStatHandler.add_new_account_stat(stat)
                if(res):
                    return jsonify("Stat created with ID {}".format(stat)), HttpStatus.OK.value
                else:
                    StatHandler.delete_stat(stat)
                    return jsonify(reason="Could not update all accounts."), HttpStatus.INTERNAL_SERVER_ERROR.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def update_stat(id, json):
        try:
            stat = statDao.update_stat(id, json)
            if not stat:
                return jsonify("Stat not found"), HttpStatus.NOT_FOUND.value
            return jsonify("Stat successfully updated"), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_stat(id):
        try:
            stat = statDao.delete_stat(id)
            if not stat:
                return jsonify("Stat not found."), HttpStatus.NOT_FOUND.value
            return jsonify("Stat deleted"), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value
        
    
