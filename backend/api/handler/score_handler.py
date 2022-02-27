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