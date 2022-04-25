from database.dao import scoreDAO
from flask import jsonify
from api import HttpStatus
from api.common.utils import sql_to_dict

class ScoreHandler:

    def get_all_scores():
        try:
            score_dao = scoreDAO.get_all_scores()
            result = []
            for s in score_dao:
                s = sql_to_dict(s)
                result.append(s)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_high_scores():
        try:
            score_dao = scoreDAO.get_high_scores()
            result = []
            for s, a, g in score_dao:
                s = sql_to_dict(s)
                a = {"username": a}
                g = {"name": g}
                result.append(s | a | g)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_high_scores_today():
        try:
            score_dao = scoreDAO.get_high_scores_today()
            result = []
            for s, a, g in score_dao:
                s = sql_to_dict(s)
                a = {"username": a}
                g = {"name": g}
                result.append(s | a | g)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_high_scores_yesterday():
        try:
            score_dao = scoreDAO.get_high_scores_yesterday()
            result = []
            for s, a, g in score_dao:
                s = sql_to_dict(s)
                a = {"username": a}
                g = {"name": g}
                result.append(s | a | g)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_high_scores_weekly():
        try:
            score_dao = scoreDAO.get_high_scores_weekly()
            result = []
            for s, a, g in score_dao:
                s = sql_to_dict(s)
                a = {"username": a}
                g = {"name": g}
                result.append(s | a | g)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value


    def get_high_scores_by_game(gid):
        try:
            score_dao = scoreDAO.get_high_scores_by_game(gid)
            result = []
            for s, a in score_dao:
                s = sql_to_dict(s)
                a = {"username": a}
                result.append(s | a)
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
                s = sql_to_dict(s)
                result.append(s)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_game_scores(game):
        try:
            score_dao = scoreDAO.get_game_scores(game)
            result = []
            for s in score_dao:
                s = sql_to_dict(s)
                result.append(s)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_user_game_scores(json):
        try:
            score_dao = scoreDAO.get_user_game_scores(json)
            result = []
            for s in score_dao:
                s = sql_to_dict(s)
                result.append(s)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_score_id(sid):
        try:
            score_dao = scoreDAO.get_score_id(sid)
            score_dao = sql_to_dict(score_dao)
            if score_dao:
                return jsonify(score_dao), HttpStatus.OK.value
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
                s = sql_to_dict(s)
                result.append(s)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_scores_game(gid):
        try:
            score_dao = scoreDAO.delete_scores_game(gid)
            result = []
            for s in score_dao:
                s = sql_to_dict(s)
                result.append(s)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def get_latest_played(uid, limit):
        try:
            score_dao = scoreDAO.get_latest_played(uid, limit)
            result = []
            for s in score_dao:
                result.append(dict(s))
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value
