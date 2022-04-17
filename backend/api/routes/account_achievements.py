from flask import request
from api import app
from api.handler.account_achievements import AccountAchievementsHandler

@app.route("/signy/account-achievement", methods=['GET', 'POST'])
def get_all_account_achievements_or_create():
    if request.method == 'GET':
        return AccountAchievementsHandler.get_all_account_achievements()
    else:
        return AccountAchievementsHandler.create_account_achievements(request.json)

@app.route("/signy/account-achievement/<int:id>", methods= ['GET', 'PUT', 'DELETE'])
def account_achievements_by_id(id):
    if request.method == 'GET':
        return AccountAchievementsHandler.get_account_achievements_id(id)
    elif request.method == 'PUT':
        return AccountAchievementsHandler.update_account_achievements(id, request.json)
    else:
        return AccountAchievementsHandler.delete_account_achievements(id)

@app.route("/signy/user-account-achievement/<int:id>", methods=['GET'])
@app.route("/signy/user-account-achievement/<int:id>/<int:gid>", methods=['GET'])
def get_user_account_achievement(id, gid=None):
    if request.method == 'GET':
        return AccountAchievementsHandler.get_user_account_achievement(id, gid)