from datetime import datetime, timedelta, timezone
from ..entity import score, account, game
from api import db
from sqlalchemy import func, text


class ScoreDAO:

    @staticmethod  # Pulls all the scores
    def get_all_scores():
        return score.query.all()

    def get_high_scores():
        return db.session.query(score, account.username, game.name).filter(score.account_id == account.id).filter(score.game_id == game.id).order_by(score.score.desc()).limit(15)
        
    def get_high_scores_by_game(gid):
        return db.session.query(score, account.username).filter(score.account_id == account.id).filter(gid == score.game_id).order_by(score.score.desc()).limit(15)

    def get_high_scores_today():
        today = datetime.now().strftime("%a, %d %b %Y")
        return db.session.query(score, account.username, game.name).filter(score.account_id == account.id).filter(score.game_id == game.id).filter(
            func.Date(score.date_achieved - timedelta(hours=4)) == today).order_by(score.score.desc()).limit(15)

    def get_high_scores_yesterday():
        yesterday = datetime.now() - timedelta(days=1)
        yesterday = yesterday.strftime("%a, %d %b %Y")
        return db.session.query(score, account.username, game.name).filter(score.account_id == account.id).filter(score.game_id == game.id).filter(
            func.Date(score.date_achieved - timedelta(hours=4)) == yesterday).order_by(score.score.desc()).limit(15)

    def get_high_scores_weekly():
        start = datetime.now() - timedelta(days=7)
        end = datetime.now()
        return db.session.query(score, account.username, game.name).filter(score.account_id == account.id).filter(score.game_id == game.id).filter(
            score.date_achieved - timedelta(hours=4) >= start).filter(score.date_achieved - timedelta(hours=4) <= end).order_by(score.score.desc()).limit(15)

    @staticmethod  # Creates new score
    def create_score(json):
        new_score = score(score=json['score'], account_id=json['account_id'],
                          game_id=json['game_id'])
        db.session.add(new_score)
        db.session.commit()
        return new_score.id

    @staticmethod  # Pulls all scores tied to specific user
    def get_user_scores(uid):
        return db.session.query(score).filter(score.account_id == uid)

    @staticmethod  # Pulls all scores tied to specific game
    def get_game_scores(gid):
        return db.session.query(score).filter(score.game_id == gid)

    @staticmethod  # Pulls all scores tied to specific user and game (ex. All User 1 scores from Hangman)
    def get_user_game_scores(json):
        return db.session.query(score).filter(score.account_id == json['account_id'], score.game_id == json['game_id'])
    
    @staticmethod # Pull latest games played plus the score for a User (can be limited with the use of the limit variable)
    def get_latest_played(uid, limit):
        op_limit = ""
        if(limit > 0):
            op_limit = "limit({})".format(limit)
        
        t = text('''SELECT score, name, date_achieved, "Score".id
                FROM "Score"
                inner join "Game" G
                on "Score".game_id = G.id and "Score".account_id = {}
                order by date_achieved desc {}'''.format(uid, op_limit)
            )
        result = db.session.execute(t)
        return result

    @staticmethod  # Pulls a score by its id
    def get_score_id(sid):
        return score.query.get(sid)

    @staticmethod  # Deletes a score by its id
    def delete_score(sid):
        score_deleted = db.session.query(score).where(score.id == sid).delete()
        db.session.commit()
        return score_deleted

    @staticmethod  # Deletes every score tied to a user
    def delete_scores_user(uid):
        scores_deleted = db.session.query(score).where(score.account_id == uid).delete()
        db.session.commit()
        return scores_deleted

    @staticmethod  # Deletes every score tied to a game
    def delete_scores_game(gid):
        scores_deleted = db.session.query(score).where(score.game_id == gid).delete()
        db.session.commit()
        return scores_deleted

