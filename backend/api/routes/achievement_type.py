from flask import request
from api import app
from api.handler.achievement_type import AchievementTypeHandler

@app.route("/signy/achievement-type", methods=['GET', 'POST'])
def get_all_achievement_types_or_create():
    if request.method == 'GET':
        return AchievementTypeHandler.get_all_achievement_types()
    else:
        return AchievementTypeHandler.create_achievement_type(request.json)

@app.route("/signy/achievement-type/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def achievement_type_by_id(id):
    if request.method == 'GET':
        return AchievementTypeHandler.get_achievement_type_by_id(id)
    elif request.method == 'PUT':
        return AchievementTypeHandler.update_achievement_type(id, request.json)
    else:
        return AchievementTypeHandler.delete_achievement_type(id)

