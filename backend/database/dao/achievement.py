from ..entity import achievement
from api import db
from datetime import datetime

class AchievementDAO:

    @staticmethod
    def get_all_achievements():
        return achievement.query.all()

    @staticmethod
    def get_achievement_id(aid):
        return achievement.query.get(aid)

    @staticmethod
    def create_achievement(json):
        new_achievement = achievement(stats_id=json['stats_id'], 
                game_id=json['game_id'], name=json['name'], type=json['type'], task=json['task'],
                description=json['description'], date_created=datetime.utcnow())
        db.session.add(new_achievement)
        db.session.commit()
        return new_achievement.id
    
    # Will not update date_created
    @staticmethod
    def update_achievement(aid, json):
        get_achievement = db.session.query(achievement).where(achievement.id == aid).update({'name':json['name'], 'type':json['type'], 'task':json['task'], 'description':json['description']})
        db.session.commit()
        return get_achievement
    
    @staticmethod
    def delete_achievement(aid):
        d_achievement = db.session.query(achievement).where(achievement.id == aid).delete()
        db.session.commit()
        return d_achievement

    @staticmethod
    def get_game_achievements(gid):
        game_achievements = db.session.query(achievement).filter(achievement.game_id == gid).order_by(achievement.id.asc()).all()
        return game_achievements