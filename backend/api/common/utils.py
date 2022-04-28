from api import db
from database.entity import *
from sqlalchemy.sql import func
from passlib.hash import pbkdf2_sha256 as sha256


# Pass sql object to function, convert into dictionary
def sql_to_dict(obj):
    obj = obj.__dict__
    obj.pop('_sa_instance_state', None)
    return obj

# @params
# start: start of the range
# end: end of range (exclusive) we add the +1
# step: amount to increment on each iteration
# Create Achievement
def create_achievement(stats_id, game_id, name, type, description, start, end, step=None):
    for x in range(start, end+1, step):

        new_achievement = achievement(stats_id=stats_id,
            game_id=game_id,
            name=name.format(x),
            type=type,
            task=x,
            description=description.format(x))

        db.session.add(new_achievement)

def initializeDB():

    #Accounts
    # new_account = account(username="yamil9926", email="yamil.irizarry@upr.edu", password=sha256.hash("password"), DOB=func.now(), first_name="Yamil", last_name="Irizarry", 
    #                             date_created=func.now(), date_updated=func.now(), role="Admin")
    # db.session.add(new_account)
    # new_account = account(username="jose_a", email="jose.biescas@upr.edu", password=sha256.hash("123456"), DOB=func.now(), first_name="Jose", last_name="Biescas", 
    #                             date_created=func.now(), date_updated=func.now(), role="Admin")
    # db.session.add(new_account)

    #Games
    new_game = game(name="Spelling Words", description="Spell the given words using the proper ASL sign.", rules="1. Spell the given word!", type="word")
    db.session.add(new_game)
    new_game = game(name="Spelling Letters", description="Spell the given letters one by one using the proper ASL sign.", rules="1. Spell the given letters before time runs out!", type="letter")
    db.session.add(new_game)
    new_game = game(name="Hang Man", description="Try to guess the word", rules="1. Guess all the letters in the word/n2. Get 10 wrong guesses and you lose", type="hangman")
    db.session.add(new_game)
    new_game = game(name="Wordle", description="Use knowledge and luck to guess the word in as few tries as possible!", rules="1. You have six chances to guess the secret word. Type in a word as a guess, and the game tells you which letters are or aren't in the word. The aim is to figure out the secret word with the fewest guesses./n 2. Clicking on a letter in the current row will delete the letter and allow you to input another one.", type="wordle")
    db.session.add(new_game)

    #Stat
    new_stat = stat(name="Words Spelled", description="Tracks number of spelled words for the game Spelling Words.", type="word")
    db.session.add(new_stat)
    new_stat = stat(name="Letters Spelled", description="Tracks number of spelled letters for the game Spelling Letters.", type="letter")
    db.session.add(new_stat)
    new_stat = stat(name="Hang Man Solved", description="Tracks number of hang man puzzles solved for the game Hang Man.", type="hangman")
    db.session.add(new_stat)
    new_stat = stat(name="Wordle Solved", description="Tracks number of worlde puzzles solved for the game Wordle.", type="wordle")
    db.session.add(new_stat)

    #Achievements
    new_achievement = achievement(stats_id=1, game_id=1, name="Spell 1 word", type="word", task=1, description="Nice job! You spelled your first word!")
    db.session.add(new_achievement)
    new_achievement = achievement(stats_id=1, game_id=1, name="Spell 10 word", type="word", task=10, description="Getting warmed up! You've spelled 10 words!")
    db.session.add(new_achievement)
    new_achievement = achievement(stats_id=1, game_id=1, name="Spell 50 word", type="word", task=50, description="You're a natural! You've spelled 50 words!")
    db.session.add(new_achievement)
    new_achievement = achievement(stats_id=1, game_id=1, name="Spell 100 word", type="word", task=100, description="Outstanding! You've spelled 100 words!")
    db.session.add(new_achievement)
    new_achievement = achievement(stats_id=1, game_id=1, name="Spell 200 word", type="word", task=200, description="You're now a master, congratulations on spelling 200 words")
    db.session.add(new_achievement)

    new_achievement = achievement(stats_id=3, game_id=3, name="Solve 1 Hang Man Puzzles", type="hangman", task=1, description="Nice job! You solved your first puzzle!")
    db.session.add(new_achievement)
    new_achievement = achievement(stats_id=3, game_id=3, name="Solve 10 Hang Man Puzzles", type="hangman", task=10, description="Getting warmed up! You've solved 10 puzzles!")
    db.session.add(new_achievement)
    new_achievement = achievement(stats_id=3, game_id=3, name="Solve 50 Hang Man Puzzles", type="hangman", task=50, description="You're a natural! You've solved 50 puzzles!")
    db.session.add(new_achievement)
    new_achievement = achievement(stats_id=3, game_id=3, name="Solve 100 Hang Man Puzzles", type="hangman", task=100, description="Outstanding! You've solved 100 puzzles!")
    db.session.add(new_achievement)
    new_achievement = achievement(stats_id=3, game_id=3, name="Solve 200 Hang Man Puzzles", type="hangman", task=200, description="You're now a master, congratulations on solving 200 puzzles")
    db.session.add(new_achievement)

    new_achievement = achievement(stats_id=4, game_id=4, name="Solve 1 Wordle Puzzles", type="wordle", task=1, description="Nice job! You solved your first puzzle!")
    db.session.add(new_achievement)
    new_achievement = achievement(stats_id=4, game_id=4, name="Solve 10 Wordle Puzzles", type="wordle", task=10, description="Getting warmed up! You've solved 10 puzzles!")
    db.session.add(new_achievement)
    new_achievement = achievement(stats_id=4, game_id=4, name="Solve 50 Wordle Puzzles", type="wordle", task=50, description="You're a natural! You've solved 50 puzzles!")
    db.session.add(new_achievement)
    new_achievement = achievement(stats_id=4, game_id=4, name="Solve 100 Wordle Puzzles", type="wordle", task=100, description="Outstanding! You've solved 100 puzzles!")
    db.session.add(new_achievement)
    new_achievement = achievement(stats_id=4, game_id=4, name="Solve 200 Wordle Puzzles", type="wordle", task=200, description="You're now a master, congratulations on solving 200 puzzles")
    db.session.add(new_achievement)

    new_asset = game_asset(name="thumbnail", description="Spelling Words", type="Picture", path="https://signy-asl-models.s3.amazonaws.com/gameImages/spellingWords.jpg", 
                            date_created=func.now(), date_updated=func.now(), game_id=1)
    db.session.add(new_asset)
    new_asset = game_asset(name="thumbnail", description="Spelling Letters", type="Picture", path="https://signy-asl-models.s3.amazonaws.com/gameImages/spellingLetters.jpg", 
                            date_created=func.now(), date_updated=func.now(), game_id=2)
    db.session.add(new_asset)
    new_asset = game_asset(name="thumbnail", description="Hang Man", type="Picture", path="https://signy-asl-models.s3.amazonaws.com/gameImages/hangman.jpg", 
                            date_created=func.now(), date_updated=func.now(), game_id=3)
    db.session.add(new_asset)
    new_asset = game_asset(name="thumbnail", description="Wordle", type="Picture", path="https://signy-asl-models.s3.amazonaws.com/gameImages/wordle.jpg", 
                            date_created=func.now(), date_updated=func.now(), game_id=4)
    db.session.add(new_asset)
    db.session.commit()
    return True