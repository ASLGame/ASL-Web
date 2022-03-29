from ..entity import achievement
from api import db
from datetime import datetime

class AchievementDAO:
    def get_all_achievements():
        return achievement.query.all()

    def get_achievement_id(aid):
        return achievement.query.get(aid)

    def create_achievement(json):
        new_achievement = achievement(account_stats_id=json['account_stats_id'], 
                game_id=json['game_id'], name=json['name'], type=json['type'], task=json['task'],
                description=json['description'], date_created=datetime.utcnow())
        db.session.add(new_achievement)
        db.session.commit()
        return new_achievement.id
    
    # Will not update date_created
    def update_achievement(aid, json):
        get_achievement = db.session.query(achievement).where(achievement.id == aid).update({'name':json['name'], 'type':json['type'], 'task':json['task'], 'description':json['description']})
        db.session.commit()
        return get_achievement
    
    def delete_achievement(aid):
        d_achievement = db.session.query(achievement).where(achievement.id == aid).delete()
        db.session.commit()
        return d_achievement