from ..entity import game
from api import db
from sqlalchemy import desc, func, and_, or_
from sqlalchemy.sql import select
from ..entity import score


class GameDao: 
    
    @staticmethod
    def get_all_games():
        return game.query.all()
    
    @staticmethod
    def create_game(json):
        new_game = game(name=json['name'], description=json['description'], rules=json['rules'], type=json['type'], date_created=json['date_created'], bank_id=json['bank_id'])
        db.session.add(new_game)
        db.session.commit()

        return new_game.id
    
    @staticmethod
    def get_game_by_id(gid):
        return game.query.get(gid)

    @staticmethod
    def get_game_by_name(name): 
        return db.session.query(game).where(game.name == name).first()

    @staticmethod
    def delete_game(gid):
        game_deleted = db.session.query(game).where(game.id==gid).delete()
        db.session.commit()
        return game_deleted

    @staticmethod
    def update_game(gid, json):
        game_updated = db.session.query(game).where(game.id==gid).update({"name": json['name'], "description":json['description'], "rules":json['rules'], "type":json['type']})
        db.session.commit()
        return game_updated

    @staticmethod
    def newest_game():
        newest_game = db.session.query(game).order_by(desc(game.date_created)).first()
        return newest_game

    @staticmethod
    def featured_games():
        subquery = db.session.query(score.game_id).group_by(score.game_id).order_by(func.count(score.game_id)).limit(3).subquery()
        featured_games = db.session.query(game).join(score).filter(game.id.in_(select(subquery))).all()
        if not featured_games or len(featured_games) < 2:
            featured_games = game.query.limit(3).all()
        return featured_games