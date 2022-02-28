from database.dao import bankDao
from flask import jsonify
from api import HttpStatus
from api.common.utils import sql_to_dict

class BankHandler:

    def get_all_banks():
        try:
            bank_dao = bankDao.get_all_banks()
            result = []
            for g in bank_dao:
                g = sql_to_dict(g)
                result.append(g)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def create_bank(json):
        try:
            bank_dao = bankDao.create_bank(json)
            if bank_dao:
                return jsonify(bank_dao), HttpStatus.CREATED.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_bank_by_id(bid):
        try:
            bank_dao = bankDao.get_bank_by_id(bid)
            bank_dao = sql_to_dict(bank_dao)
            if bank_dao:
                return jsonify(bank_dao), HttpStatus.OK.value
            else:
                return jsonify("Bank with ID: {} not found".format(bid)), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_bank(bid):
        try:
            bank_dao_deleted = bankDao.delete_bank(bid)
            if bank_dao_deleted:
                return jsonify("Bank deleted successfully"), HttpStatus.OK.value
            else:
                return jsonify("Bank not found"), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def update_bank(bid, json):
        try:
            bank_dao_updated = bankDao.update_bank(bid, json)
            if bank_dao_updated:
                return jsonify(bank_dao_updated), HttpStatus.OK.value
            else:
                return jsonify("Bank not found"), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value 