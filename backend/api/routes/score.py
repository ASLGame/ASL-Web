import re
from flask import request
from api import app
from api.handler.score_handler import ScoreHandler

@app.route("/signy/scores", methods=['GET', 'POST'])
def get_all_scores_or_create():
    if request.method == 'GET':
        return ScoreHandler.get_all_scores()
    elif request.method == 'POST':
        return ScoreHandler.create_score(request.json)

@app.route("/signy/scores/<int:sid>", methods=['GET', 'DELETE'])
def get_delete_score_id(sid):
    if request.method == 'GET':
        return ScoreHandler.get_score_id(sid)
    elif request.method == 'DELETE':
        return ScoreHandler.delete_score(sid)

@app.route("/signy/scores/users/<int:uid>", methods=['GET', 'DELETE'])
def get_user_scores(uid):
    if request.method == 'GET':
        return ScoreHandler.get_user_scores(uid)
    elif request.method == 'DELETE':
        return ScoreHandler.delete_scores_user(uid)

@app.route("/signy/scores/games/<int:gid>", methods=['GET', 'DELETE'])
def get_game_scores(gid):
    if request.method == 'GET':
        return ScoreHandler.get_game_scores(gid)
    elif request.method == 'DELETE':
        return ScoreHandler.delete_scores_game(gid)

@app.route("/signy/scores/users/latest/<int:uid>", methods=['GET'])
def get_latest_played(uid):
    if request.method == 'GET':
        return ScoreHandler.get_latest_played(uid)