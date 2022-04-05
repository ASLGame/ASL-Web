from flask import request
from api import app
from api.handler.achievement import AchievementHandler

@app.route("/signy/achievement", methods=['GET', 'POST'])
def get_all_achievements_or_create():
    if request.method == 'GET':
        return AchievementHandler.get_all_achievements()
    else:
        return AchievementHandler.create_achievement(request.json)

@app.route("/signy/achievement/<int:id>", methods= ['GET', 'PUT', 'DELETE'])
def achievement_by_id(id):
    if request.method == 'GET':
        return AchievementHandler.get_achievement_id(id)
    elif request.method == 'PUT':
        return AchievementHandler.update_achievement(id, request.json)
    else:
        return AchievementHandler.delete_achievement(id)