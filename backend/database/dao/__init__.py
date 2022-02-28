from .account import AccountDao
from .game import GameDao
from .stat import StatDao
from .account_stat import AccountStatDao
from .achievement_type import AchievementTypeDao
from .score import ScoreDAO
from .bank import BankDao

bankDao = BankDao
accountDAO = AccountDao
gameDao = GameDao
statDao = StatDao
accountStatDao = AccountStatDao
achievementTypeDao = AchievementTypeDao
scoreDAO = ScoreDAO
