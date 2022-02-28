from database.dao import wordDao
from flask import jsonify
from api import HttpStatus
from api.common.utils import sql_to_dict

class WordHandler:

    def get_all_words():
        try: 
            words = wordDao.get_all_words()
            result = []
            for word in words:
                dictWord = sql_to_dict(word)
                result.append(dictWord)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value
        
    def get_word_by_id(id):
        try: 
            word = wordDao.get_word_by_id(id)
            if not word:
                return jsonify("Word with ID: {} not found.".format(id)), HttpStatus.NOT_FOUND.value
            result = sql_to_dict(word)
            return jsonify(result), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def create_word(json):
        try: 
            word_created = wordDao.create_word(json)
            return jsonify("Word with ID: {} created successfully.".format(word_created)), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value
        
    def update_word(id, json):
        try:
            word_updated = wordDao.update_word(id, json)
            if not word_updated:
                return jsonify("Word not found."), HttpStatus.NOT_FOUND.value
            return jsonify("Word updated successfully"), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

    def delete_word(id):
        try: 
            word_deleted = wordDao.delete_word(id)
            if not word_deleted:
                return jsonify("Word not found."), HttpStatus.NOT_FOUND.value
            return jsonify("Word successfully deleted."), HttpStatus.OK.value
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), HttpStatus.INTERNAL_SERVER_ERROR.value

