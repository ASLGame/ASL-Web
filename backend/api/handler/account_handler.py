from datetime import timedelta
from database.dao import accountDAO
from flask import jsonify
from api import HttpStatus, app
from api.common.utils import sql_to_dict
from itsdangerous import URLSafeTimedSerializer
from api.common.email import send_email
from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256 as sha256

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

    def get_account_id(uid):
        try:
            account_dao = accountDAO.get_account_id(uid)
            if account_dao:
                account_dao = sql_to_dict(account_dao)
                return jsonify(account_dao), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_account_username(uname):
        try:
            account_dao = accountDAO.get_account_username(uname)
            result = []
            if account_dao:
                for a in account_dao:
                    a = sql_to_dict(a)
                    result.append(a)
                return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_account_DOB(DOB):
        try:
            account_dao = accountDAO.get_account_DOB(DOB)
            result = []
            if account_dao:
                for a in account_dao:
                    a = sql_to_dict(a)
                    result.append(a)
                return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_account_fn(fname):
        try:
            account_dao = accountDAO.get_account_fn(fname)
            result = []
            if account_dao:
                for a in account_dao:
                    a = sql_to_dict(a)
                    result.append(a)
                return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_account_ln(lname):
        try:
            account_dao = accountDAO.get_account_ln(lname)
            result = []
            if account_dao:
                for a in account_dao:
                    a = sql_to_dict(a)
                    result.append(a)
                return jsonify(result), HttpStatus.OK.value
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

    def sign_in(json):
        try:
            account_dao = accountDAO.get_account_username(json['username'])
            if account_dao:
                account_dao = sql_to_dict(account_dao)
                if(sha256.verify(json['password'], account_dao['password'])):
                    access_token = create_access_token(identity=account_dao['id'], expires_delta=timedelta(days=5))
                    return jsonify(access_token = access_token, account_id = account_dao['id'], account_username = account_dao['username'], account_firstname = account_dao['first_name'], account_created = account_dao['date_created'], account_email = account_dao['email'], account_role=account_dao['role']), HttpStatus.OK.value
                else:
                    return jsonify(reason="Password did not match"), HttpStatus.BAD_REQUEST.value
            return jsonify(reason="Username not found"), HttpStatus.BAD_REQUEST.value
        except Exception as e:
             return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def sign_up(json):
        try:    
            account_dao = accountDAO.get_account_email(json['email'])
            if account_dao:
                return jsonify(reason="Account with given email already exists."), HttpStatus.BAD_REQUEST.value
            username_exists = accountDAO.get_account_username(json['username'])
            if username_exists:
                return jsonify(reason="Username already taken"), HttpStatus.BAD_REQUEST.value
            create_account = accountDAO.create_account(json)
            token = AccountHandler.generate_confirmation_token(json.get('email'))
            send_email(json['email'], "Email Confirmation Code", token)
            return AccountHandler.sign_in(json)
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def confirm_email(token):
        try: 
            email = AccountHandler.confirm_token(token)
        except Exception as e:
            return jsonify(reason="The confirmation link has expired.", error=e.__str__()), HttpStatus.BAD_REQUEST.value
        account = accountDAO.get_account_email(email)
        if account.email_confirmed:
            return jsonify(reason="This account has already been confirmed"),  HttpStatus.OK.value
        else:
            accountDAO.confirm_account(account.id)
            return jsonify("Account successfully confirmed"), HttpStatus.OK.value
                
    def confirm_token(token, expiration=3600):
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        try:
            email = serializer.loads(
                token,
                salt=app.config['SECRET_SALT'],
                max_age=expiration
            )
        except:
            return False
        return email
    
    def generate_confirmation_token(email):
                serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
                return serializer.dumps(email, salt=app.config['SECRET_SALT'])