from curses.ascii import HT
import http
from database.dao import scoreDAO
from flask import jsonify
from api import HttpStatus

class ScoreHandler:

    def get_all_scores():
        try:
            score_dao = scoreDAO.get_all_scores()
            result = []
            for s in score_dao:
                result.append(s)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def create_score(json):
        try:
            score_dao = scoreDAO.create_score(json)
            if score_dao:
                return jsonify(score_dao), HttpStatus.CREATED.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_user_scores(account):
        try:
            score_dao = scoreDAO.get_user_scores(account)
            result = []
            for s in score_dao:
                result.append(s)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_game_scores(game):
        try:
            score_dao = scoreDAO.get_game_scores(game)
            result = []
            for s in score_dao:
                result.append(s)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_user_game_scores(json):
        try:
            score_dao = scoreDAO.get_user_game_scores(json)
            result = []
            for s in score_dao:
                result.append(s)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_score_id(sid):
        try:
            score_dao = scoreDAO.get_score_id(sid)
            if score_dao:
                return jsonify(score_dao.as_dict()), HttpStatus.OK.value
            else:
                return jsonify("Score with ID: {} not found".format(sid)), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_score(sid):
        try:
            score_dao = scoreDAO.delete_score(sid)
            if score_dao:
                return jsonify("Score deleted successfully"), HttpStatus.OK.value
            else:
                return jsonify("Score not found"), HttpStatus.NOT_FOUND.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_scores_user(uid):
        try:
            score_dao = scoreDAO.delete_scores_user(uid)
            result = []
            for s in score_dao:
                result.append(s)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_scores_game(gid):
        try:
            score_dao = scoreDAO.delete_scores_game(gid)
            result = []
            for s in score_dao:
                result.append(s)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

