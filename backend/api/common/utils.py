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
    new_account = account(username="jose_a", email="jose.biescas@upr.edu", password="123456", DOB=func.now(), first_name="Jose", last_name="Biescas", 
                                date_created=func.now(), date_updated=func.now(), role="Admin")
    db.session.add(new_account)
    new_bank = bank(name="Bank", description="Description")
    db.session.add(new_bank)
    new_game = game(name="Game One", description="A game you can play", rules="1. Dont talk about Fight Club", type="Text", date_created=func.now(), bank_id=1)
    db.session.add(new_game)
    new_game = game(name="Game Two", description="Another game you can play", rules="1. Dont talk about Fight Club", type="Text", date_created=func.now(), bank_id=1)
    db.session.add(new_game)
    new_game = game(name="Game Three", description="Yet another game you can play", rules="1. Dont talk about Fight Club", type="Text", date_created=func.now(), bank_id=1)
    db.session.add(new_game)
    new_score = score(score=420, date_achieved=func.now(), account_id=1, game_id=1)
    db.session.add(new_score)
    new_stat = stat(name="Words Spelled", description="Number of spelled words", type="Word")
    db.session.add(new_stat)
    new_account_stat = account_stat(account_id=1, stats_id=1, value=0, date_created=func.now(), date_updated=func.now())
    db.session.add(new_account_stat)
    new_account_stat = account_stat(account_id=2, stats_id=1, value=0, date_created=func.now(), date_updated=func.now())
    db.session.add(new_account_stat)
    new_achievement = achievement(name="Spell 10 words", type="Word", description="User has to spell 10 words", date_created=func.now(), task=10, stats_id=1, game_id=1)
    db.session.add(new_achievement)
    new_achievement = achievement(name="Spell 20 words", type="Word", description="User has to spell 20 words", date_created=func.now(), task=20, stats_id=1, game_id=1)
    db.session.add(new_achievement)
    new_achievement = achievement(name="Spell 30 words", type="Word", description="User has to spell 30 words", date_created=func.now(), task=30, stats_id=1, game_id=1)
    db.session.add(new_achievement)
    new_account_achievement = account_achievements(account_id=1, has_achieved=False, date_created=func.now(), date_updated=func.now(), achievement_id=1)
    db.session.add(new_account_achievement)
    new_account_achievement = account_achievements(account_id=1, has_achieved=False, date_created=func.now(), date_updated=func.now(), achievement_id=2)
    db.session.add(new_account_achievement)
    new_account_achievement = account_achievements(account_id=1, has_achieved=False, date_created=func.now(), date_updated=func.now(), achievement_id=3)
    db.session.add(new_account_achievement)
    new_account_achievement = account_achievements(account_id=2, has_achieved=False, date_created=func.now(), date_updated=func.now(), achievement_id=1)
    db.session.add(new_account_achievement)
    new_account_achievement = account_achievements(account_id=2, has_achieved=False, date_created=func.now(), date_updated=func.now(), achievement_id=2)
    db.session.add(new_account_achievement)
    new_account_achievement = account_achievements(account_id=2, has_achieved=False, date_created=func.now(), date_updated=func.now(), achievement_id=3)
    db.session.add(new_account_achievement)
    new_score = score(score=2134, date_achieved=func.now(), account_id=1, game_id=1)
    db.session.add(new_score)
    new_score = score(score=3213, date_achieved=func.now(), account_id=1, game_id=1)
    db.session.add(new_score)
    new_score = score(score=7557, date_achieved=func.now(), account_id=1, game_id=1)
    db.session.add(new_score)
    new_score = score(score=3453, date_achieved=func.now(), account_id=1, game_id=1)
    db.session.add(new_score)
    new_score = score(score=8678, date_achieved=func.now(), account_id=1, game_id=1)
    db.session.add(new_score)
    new_score = score(score=7689, date_achieved=func.now(), account_id=1, game_id=1)
    db.session.add(new_score)
    new_score = score(score=4234, date_achieved=func.now(), account_id=2, game_id=2)
    db.session.add(new_score)
    new_score = score(score=1235, date_achieved=func.now(), account_id=2, game_id=1)
    db.session.add(new_score)
    new_score = score(score=6456, date_achieved=func.now(), account_id=2, game_id=3)
    db.session.add(new_score)
    new_score = score(score=8678, date_achieved=func.now(), account_id=2, game_id=1)
    db.session.add(new_score)
    new_score = score(score=3125, date_achieved=func.now(), account_id=2, game_id=2)
    db.session.add(new_score)
    new_score = score(score=6417, date_achieved=func.now(), account_id=2, game_id=3)
    db.session.add(new_score)
    new_asset = game_asset(name="One", description="Picture of a number 1", type="Picture", path="https://cdn.vox-cdn.com/thumbor/Hgbit5XaEq1wAhGPYtb1R-kD570=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/12055117/logo_one_icon.jpg", 
                            date_created=func.now(), date_updated=func.now(), game_id=1)
    db.session.add(new_asset)
    new_asset = game_asset(name="Two", description="Picture of a number 2", type="Picture", path="https://www.freeiconspng.com/uploads/number-two-icon-18.jpg", 
                            date_created=func.now(), date_updated=func.now(), game_id=2)
    db.session.add(new_asset)
    new_asset = game_asset(name="Three", description="Picture of a number 3", type="Picture", path="https://www.nicepng.com/png/detail/38-385284_number-3-png-number-3-transparent-background.png", 
                            date_created=func.now(), date_updated=func.now(), game_id=3)
    db.session.add(new_asset)
    db.session.commit()
    return True