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

@app.route("/signy/scores/users/latest/<int:uid>")
@app.route("/signy/scores/users/latest/<int:uid>/<int:limit>", methods=['GET'])
def get_latest_played(uid, limit=0):
    if request.method == 'GET':
        return ScoreHandler.get_latest_played(uid, limit)

@app.route("/signy/scores/highscores", methods=["GET"])
def get_high_scores():
    if request.method == 'GET':
        return ScoreHandler.get_high_scores()

@app.route("/signy/scores/highscores/<int:gid>", methods=["GET"])
def get_high_scores_by_game(gid):
    if request.method == 'GET':
        return ScoreHandler.get_high_scores_by_game(gid)

@app.route("/signy/scores/highscores/today", methods=["GET"])
def get_high_scores_today():
    if request.method == 'GET':
        return ScoreHandler.get_high_scores_today()
        
@app.route("/signy/scores/highscores/yesterday", methods=["GET"])
def get_high_scores_yesterday():
    if request.method == 'GET':
        return ScoreHandler.get_high_scores_yesterday()

@app.route("/signy/scores/highscores/weekly", methods=["GET"])
def get_high_scores_weekly():
    if request.method == 'GET':
        return ScoreHandler.get_high_scores_weekly()
