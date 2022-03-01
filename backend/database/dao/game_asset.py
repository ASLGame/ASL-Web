from ..entity import game_asset
from api import db

class GameAssetDAO:

    @staticmethod  # Pulls all the game assets
    def get_all_assets():
        return game_asset.query.all()

    @staticmethod  # Deletes a game asset by its ID
    def delete_asset_id(aid):
        asset = db.session.query(game_asset).where(game_asset.id == aid).delete()
        db.session.commit()
        return asset

    @staticmethod  # Gets a game asset by it ID
    def get_asset_id(aid):
        return game_asset.query.get(aid)

    @staticmethod  # Creates a new game asset
    def create_asset(json):
        asset = game_asset(name=json['name'], description=json['description'], type=json['type'], path=json['path'], date_created=json['date_created'], date_updated=json['date_updated'], game_id=json['game_id'])
        db.session.add(asset)
        db.session.commit()
        return asset.id

    @staticmethod  # Updates a game asset
    def update_asset(aid, json):
        asset = db.session.query(game_asset).where(game_asset.id == aid).update(name=json['name'], description=json['description'], type=json['type'], path=json['path'], date_updated=json['date_updated'], game_id=json['game_id'])
        db.session.commit()
        return asset