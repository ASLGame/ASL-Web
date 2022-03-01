from database.dao import gameassetDAO
from flask import jsonify
from api import HttpStatus
from api.common.utils import sql_to_dict

class GameAssetHandler:

    def get_all_assets():
        try:
            asset = gameassetDAO.get_all_assets()
            result = []
            for a in asset:
                a = sql_to_dict(a)
                result.append(a)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_asset_id(aid):
        try:
            asset = gameassetDAO.get_asset_id(aid)
            if asset:
                return jsonify(asset), HttpStatus.OK.value
            else:
                return jsonify("Game Asset with ID: {} not found".format(aid)), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_asset_id(aid):
        try:
            asset = gameassetDAO.delete_asset_id(aid)
            if asset:
                return jsonify("Game asset deleted successfully"), HttpStatus.OK.value
            else:
                return jsonify("Game Asset not found"), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def create_game_asset(json):
        try:
            asset = gameassetDAO.create_asset(json)
            if asset:
                return jsonify(asset), HttpStatus.CREATED.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def update_game_asset(aid, json):
        try:
            asset = gameassetDAO.update_asset(aid, json)
            if asset:
                return jsonify(asset), HttpStatus.OK.value
            else:
                return jsonify("Game Asset not found"), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value