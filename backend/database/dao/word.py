from ..entity import word
from api import db

class WordDao:

    @staticmethod
    def get_all_words():
        return word.query.all()

    @staticmethod
    def get_word_by_id(id):
        return word.query.get(id)

    @staticmethod
    def create_word(json):
        word_created = word(bank_id = json['bank_id'], word = json['word'], difficulty = json['difficulty'])
        db.session.add(word_created)
        db.session.commit()

        return word_created.id

    @staticmethod
    def update_word(id, json):
        word_updated = db.session.query(word).where(word.id == id).update({ "difficulty": json['difficulty'] })
        db.session.commit()
        return word_updated

    @staticmethod
    def delete_word(id):
        word_deleted = db.session.query(word).where(word.id == id).delete()
        db.session.commit()
        return word_deleted