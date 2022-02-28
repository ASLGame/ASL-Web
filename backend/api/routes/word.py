from flask import request
from api import app
from api.handler.word import WordHandler

@app.route("/signy/word", methods=['GET', 'POST'])
def get_all_words_or_create():
    if request.method == 'GET':
        return WordHandler.get_all_words()
    elif request.method == 'POST':
        return WordHandler.create_word(request.json)

@app.route("/signy/word/<int:id>", methods=['GET', 'DELETE', 'PUT'])
def word_by_id(id):
    if request.method == 'GET':
        return WordHandler.get_word_by_id(id)
    elif request.method == 'PUT':
        return WordHandler.update_word(id, request.json)
    else:
        return WordHandler.delete_word(id)
    