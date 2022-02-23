from api import db

# Run this to create all tables.

db.drop_all()
db.create_all()