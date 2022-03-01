from ..entity import game_asset
from api import db

class GameAssetDAO:

    @staticmethod  # Pulls all the game assets
    def get_all_assets():
        return game_asset.query.all()

    @staticmethod
    def delete_asset_id(aid):
        asset = db.session.query(game_asset).where(game_asset.id == aid).delete()
        db.session.commit()
        return asset

    @staticmethod
    def get_asset_id(aid):
        return game_asset.query.get(aid)

    @staticmethod
    def create_asset(json):
        asset = game_asset(name=json['name'], description=json['description'], type=json['type'], path=json['path'], date_created=json['date_created'], date_updated=json['date_updated'], game_id=json['game_id'])
        db.session.add(asset)
        db.session.commit()
        return asset.id

    @staticmethod
    def update_asset(aid, json):
        asset = db.session.query(game_asset).where(game_asset.id == aid).update(name=json['name'], description=json['description'], type=json['type'], path=json['path'], date_updated=json['date_updated'], game_id=json['game_id'])
        db.session.commit()
        return asset