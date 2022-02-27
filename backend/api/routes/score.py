import re
from flask import request
from api import app
from api.handler.score_handler import ScoreHandler

@app.route("signy/scores", methods=['GET', 'POST'])
def get_create_scores():
    if request.method == 'GET':
        return ScoreHandler.get_all_scores()
    elif request.method == 'POST':
        return ScoreHandler.create_score(request.json)