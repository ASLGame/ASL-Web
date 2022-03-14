from api import db
from api.common.utils import dummyDB

# Run this to create all tables.
flag = input("Are you sure you want to recreate database? (y/n)")
if(flag == 'y'):
    db.drop_all()
    db.create_all()
    dummyDB()
    print("Recreated DB.")
else:
    print("Aborted recreating DB.")
