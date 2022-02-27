from ..entity import game
from api import db
from flask import jsonify

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
    def delete_game(gid):
        game_deleted = db.session.query(game).where(game.id==gid).delete()
        db.session.commit()
        return game_deleted

    @staticmethod
    def update_game(gid, json):
        game_updated = db.session.query(game).where(game.id==gid).update({"name": json['name'], "description":json['description'], "rules":json['rules'], "type":json['type']})
        db.session.commit()
        return game_updated