from database.dao.achievement import AchievementDAO
from database.dao.account import AccountDao
from ..entity import account_achievements
from api import db
from datetime import datetime
from sqlalchemy import text

class AccountAchievementsDAO:
    
    @staticmethod
    def get_all_account_achievements():
        return account_achievements.query.all()
    
    @staticmethod
    def get_account_achievements_id(aid):
        return account_achievements.query.get(aid)

    @staticmethod
    def create_account_achievements(json):
        new_account_achievement = account_achievements(account_id=json['account_id'], 
                achievement_id=json['achievement_id'], has_achieved=json.get('has_achieved'), 
                date_achieved=json.get('date_achieved'),date_created=datetime.utcnow(), 
                date_updated=datetime.utcnow())
        db.session.add(new_account_achievement)
        db.session.commit()
        return new_account_achievement.id
    
    @staticmethod
    # Will not update date_created
    def update_account_achievements(aid, json):
        get_account_achievement = db.session.query(account_achievements).where(account_achievements.id == aid).update({'has_achieved':json['has_achieved'], 
                'date_achieved': json.get('date_achieved'), 
                'date_updated': datetime.utcnow()})
        db.session.commit()
        return get_account_achievement
    
    @staticmethod
    def delete_account_achievements(aid):
        d_achievement = db.session.query(account_achievements).where(account_achievements.id == aid).delete()
        db.session.commit()
        return d_achievement
    
    @staticmethod
    def get_user_account_achievement(id, gid):
        if gid:
            t = text('''
        SELECT game_id, AACH.account_id as account_id, AACH.id as acc_ach_id, AACH.has_achieved, A.name, A.task, ASS.value, S.id as stats_id, date_achieved, A.id as achievement_id
            from "Account_Achievements" as AACH
                inner join "Achievement" as A on AACH.account_id = {} and AACH.achievement_id = A.id and A.game_id = {}
                inner join "Stats" as S on A.stats_id = S.id
                inner join "Account_Stats" as ASS on S.id = ASS.stats_id and AACH.account_id = ASS.account_id
                order by AACH.id
        '''.format(id, gid))
        else:
            t = text('''
            SELECT game_id, AACH.account_id as account_id, AACH.id as acc_ach_id, AACH.has_achieved, A.name, A.task, ASS.value, S.id as stats_id, date_achieved, A.id as achievement_id
                from "Account_Achievements" as AACH
                    inner join "Achievement" as A on AACH.account_id = {} and AACH.achievement_id = A.id
                    inner join "Stats" as S on A.stats_id = S.id
                    inner join "Account_Stats" as ASS on S.id = ASS.stats_id and AACH.account_id = ASS.account_id
                    order by game_id
            '''.format(id))

        result = db.session.execute(t)
        return result
    
    @staticmethod
    def account_achievements_initialize(id):
        achievements = AchievementDAO.get_all_achievements()
        successful = []
        for ach in achievements:
            info = {'account_id': id, 'achievement_id': ach.id}
            res = AccountAchievementsDAO.create_account_achievements(info)
            successful.append(res)
        if (len(successful) == len(achievements)):
            return True
        return False
    
    @staticmethod
    def add_new_account_achievements(aid):
        accounts = AccountDao.getAllAccounts()
        successful = []
        for acc in accounts:
            info = {'account_id': acc.id, 'achievement_id': aid}
            res = AccountAchievementsDAO.create_account_achievements(info)
            successful.append(res)
        if (len(successful) == len(accounts)):
            return True
        return False