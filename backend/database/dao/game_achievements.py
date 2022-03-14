from ..entity import game_achievement
from api import db

class GameAchievementsDAO:
    def get_all_game_achievements():
        return game_achievement.query.all()

    def get_game_achievement_id(gaid):
        return game_achievement.query.get(gaid)

    def get_game_achievement_stats_id(stid):
        return db.session.query(game_achievement).where(game_achievement.stats_id == stid)

    def get_game_achievement_game_id(gid):
        return db.session.query(game_achievement).where(game_achievement.game_id == gid)

    def get_game_achievement_achievement_id(aid):
        return db.session.query(game_achievement).where(game_achievement.achievement_type_id == aid)

    def create_game_achievement(json):
        achievement = game_achievement(name=json['name'], description=json['description'], task=json['task'], achievement_type_id=json['achievement_type_id'], 
                                        stats_id = json['stats_id'], game_id = json['game_id'])
        db.session.add(achievement)
        db.session.commit()
        return achievement.id
    
    def update_game_achievement(gaid, json):
        achievement = db.session.query(game_achievement).where(game_achievement.id == gaid).update(name=json['name'], description=json['description'], task=json['task'], 
                                        achievement_type_id=json['achievement_type_id'], stats_id = json['stats_id'], game_id = json['game_id'])
        db.session.commit()
        return achievement

    def delete_game_achievement(gaid):
        achievement = db.session.query(achievement).where(game_achievement.id == gaid).delete()
        db.session.commit()
        return achievement