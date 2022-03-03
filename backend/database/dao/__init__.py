from .account import AccountDao
from .game import GameDao
from .word import WordDao
from .stat import StatDao
from .account_stat import AccountStatDao
from .achievement_type import AchievementTypeDao
from .score import ScoreDAO
from .bank import BankDao
from .game_achievements import GameAchievementsDAO

bankDao = BankDao
accountDAO = AccountDao
gameDao = GameDao
wordDao = WordDao
statDao = StatDao
accountStatDao = AccountStatDao
achievementTypeDao = AchievementTypeDao
scoreDAO = ScoreDAO
gameachievementsDAO = GameAchievementsDAO
