from api import db
from database.entity import *
from sqlalchemy.sql import func


# Pass sql object to function, convert into dictionary
def sql_to_dict(obj):
    obj = obj.__dict__
    obj.pop('_sa_instance_state', None)
    return obj

def dummyDB():
    new_account = account(username="yamil9926", email="yamil.irizarry@upr.edu", password="password", DOB=func.now(), first_name="Yamil", last_name="Irizarry", 
                                date_created=func.now(), date_updated=func.now(), role="Admin")
    db.session.add(new_account)
    new_bank = bank(name="Bank", description="Description")
    db.session.add(new_bank)
    new_game = game(name="Game One", description="A game you can play", rules="1. Dont talk about Fight Club", type="Text", date_created=func.now(), bank_id=1)
    db.session.add(new_game)
    new_score = score(score=420, date_achieved=func.now(), account_id=1, game_id=1)
    db.session.add(new_score)
    db.session.commit()
    return True