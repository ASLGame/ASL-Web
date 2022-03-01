from database.dao import accountDAO
from flask import jsonify
from api import HttpStatus
from api.common.utils import sql_to_dict

class AccountHandler:

    def get_all_accounts():
        try:
            account_dao = accountDAO.getAllAccounts()
            result = []
            for a in account_dao:
                a = sql_to_dict(a)
                result.append(a)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def create_account(json):
        try:
            new_account = accountDAO.create_account(json)
            if new_account:
                return jsonify(new_account), HttpStatus.CREATED.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_account(uid):
        try:
            account_dao = accountDAO.delete_account_id(uid)
            if account_dao:
                return jsonify("Account deleted successfully"), HttpStatus.OK.value
            else:
                return jsonify("Account not found"), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_account_username(uname):
        try:
            account_dao = accountDAO.get_account_username(uname)
            if account_dao:
                account_dao = sql_to_dict(account_dao)
                return jsonify(account_dao), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_account_DOB(DOB):
        try:
            account_dao = accountDAO.get_account_DOB(DOB)
            if account_dao:
                account_dao = sql_to_dict(account_dao)
                return jsonify(account_dao), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_account_fn(fname):
        try:
            account_dao = accountDAO.get_account_fn(fname)
            if account_dao:
                account_dao = sql_to_dict(account_dao)
                return jsonify(account_dao), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_account_ln(lname):
        try:
            account_dao = accountDAO.get_account_ln(lname)
            if account_dao:
                account_dao = sql_to_dict(account_dao)
                return jsonify(account_dao), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def update_account(uid,json):
        try:
            account_dao = accountDAO.update_account(uid,json)
            if account_dao:
                return jsonify(account_dao), HttpStatus.OK.value
            else:
                return jsonify("Account not found"), HttpStatus.NOT_FOUND.value
        except Exception as e:
             return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value
