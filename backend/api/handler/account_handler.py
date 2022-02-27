from database.dao import accountDAO
from flask import jsonify
from api import HttpStatus

class Accounthandler:

    def get_all_accounts():
        try:
            account_dao = accountDAO.getAllAccounts()
            result = []
            for a in account_dao:
                result.append(a)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value