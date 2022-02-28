from database.dao import accountStatDao
from flask import jsonify
from api import HttpStatus
from api.common.utils import sql_to_dict

class AccountStatHandler:

    def get_all_account_stats():
        try:
            account_stats = accountStatDao.get_all_account_stats()
            result = []
            for stat in account_stats:
                dictStat = sql_to_dict(stat)
                result.append(dictStat)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_account_stat_by_id(id):
        try:
            stat = accountStatDao.get_account_stat_by_id(id)
            if not stat:
                return jsonify("Account stat with ID: {} does not exist.".format(id)), HttpStatus.NOT_FOUND.value
            result = sql_to_dict(stat)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def create_account_stat(json):
        try: 
            account_stat = accountStatDao.create_account_stat(json)
            return jsonify("Account stat created with ID {}".format(account_stat)), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def update_account_stat(id, json):
        try:
            if (json.get('has_achieved')):
                
                account_stat = accountStatDao.update_achieved_account_stat(id, json)
            else:
                account_stat = accountStatDao.update_account_stat(id, json)
            if not account_stat:
                return jsonify("Account stat not found."), HttpStatus.NOT_FOUND.value
            return jsonify("Stat updated successfully"), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_account_stat(id):
        try: 
            account_stat = accountStatDao.delete_account_stat(id)
            if not account_stat:
                return jsonify("Account stat not found."), HttpStatus.NOT_FOUND.value
            return jsonify("Account stat deleted."), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value