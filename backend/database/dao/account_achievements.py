from ..entity import account_achievements
from api import db
from datetime import datetime

class AccountAchievementsDAO:
    def get_all_account_achievements():
        return account_achievements.query.all()

    def get_account_achievements_id(aid):
        return account_achievements.query.get(aid)

    def create_account_achievements(json):
        new_account_achievement = account_achievements(account_id=json['account_id'], 
                achievement_id=json['achievement_id'], has_achieved=json['has_achieved'], 
                date_achieved=json['date_achieved'], date_created=datetime.utcnow(), 
                date_updated=datetime.utcnow())
        db.session.add(new_account_achievement)
        db.session.commit()
        return new_account_achievement.id
    
    # Will not update date_created
    def update_account_achievements(aid, json):
        get_account_achievement = db.session.query(account_achievements).where(account_achievements.id == aid).update(has_achieved=json['has_achieved'], 
                date_achieved=json['date_achieved'], 
                date_updated=datetime.utcnow())
        db.session.commit()
        return get_account_achievement
    
    def delete_account_achievements(aid):
        d_achievement = db.session.query(account_achievements).where(account_achievements.id == aid).delete()
        db.session.commit()
        return d_achievement