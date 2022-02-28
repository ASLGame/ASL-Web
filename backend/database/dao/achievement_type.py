from api import db
from ..entity import achievement_type

class AchievementTypeDao: 

    @staticmethod
    def get_all_achievement_types():
        return achievement_type.query.all()

    @staticmethod
    def get_achievement_type_by_id(id):
        return achievement_type.query.get(id)

    @staticmethod
    def create_achievement_type(json):
        new_achievement_type = achievement_type(name=json['name'], description=json['description'], type=json['type'])
        db.session.add(new_achievement_type)
        db.session.commit()

        return new_achievement_type.id

    @staticmethod
    def update_achievement_type(id, json):
        update = db.session.query(achievement_type).where(achievement_type.id == id).update({"name": json['name'], "description": json['description'], "type": json['type']})
        db.session.commit()
        return update

    @staticmethod
    def delete_achievement_type(id):
        deleted = db.session.query(achievement_type).where(achievement_type.id == id).delete()
        db.session.commit()
        return deleted

