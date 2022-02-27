from ..entity import score
from api import db


class ScoreDAO:

    @staticmethod  # Pulls all the scores
    def get_all_scores():
        return score.query.all()

    @staticmethod  # Creates new score
    def create_score(json):
        new_score = score(score=json['score'], date_achieved=json['date_achieved'], account_id=json['account_id'],
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

