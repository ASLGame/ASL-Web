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
    
    def get_stat_by_type(type):
        try: 
            stat = statDao.get_stat_by_type(type)
            if len(stat) < 1:
                return jsonify("Stat with Type: {} does not exist.".format(type)), HttpStatus.NOT_FOUND.value
            res = []
            for s in stat:
                res.append(sql_to_dict(s))
            return jsonify(res), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value
    
    def create_stat(json):
        try: 
            stat = statDao.create_stat(json)
            if(stat):
                res = AccountStatHandler.add_new_account_stat(stat)
                if(res[1] == 200):
                    return jsonify("Stat created with ID {}".format(stat)), HttpStatus.OK.value
                else:
                    StatHandler.delete_stat(stat)
                    return jsonify(reason="Could not update all account stats because {}".format(res[0].get_json())), HttpStatus.BAD_REQUEST.value
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
        
    
