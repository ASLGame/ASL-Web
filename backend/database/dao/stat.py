from api import db
from ..entity import stat

class StatDao:

    @staticmethod
    def get_all_stats():
        return stat.query.all()

    @staticmethod
    def get_stat_by_id(id):
        return stat.query.get(id)

    @staticmethod
    def get_stat_by_type(type):
        return db.session.query(stat).filter(stat.type.contains(type)).all()

    @staticmethod
    def create_stat(json):
        new_stat = stat(name=json['name'], description=json['description'], type=json["type"])
        db.session.add(new_stat)
        db.session.commit()

        return new_stat.id

    @staticmethod
    def update_stat(id, json):
        update_stat = db.session.query(stat).where(stat.id == id).update({"name": json['name'], "description": json['description'], "type": json['type']})
        db.session.commit()
        return update_stat
    
    @staticmethod
    def delete_stat(id):
        delete_stat = db.session.query(stat).where(stat.id == id).delete()
        db.session.commit()
        return delete_stat