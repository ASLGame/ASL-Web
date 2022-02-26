from unicodedata import name
from ..entity import game
from api import db

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
        pass

    @staticmethod
    def delete_game(gid):
        pass

    @staticmethod
    def update_game(gid, json):
        pass