import utils
from sqlalchemy import create_engine
from utils.py import utils

engine = utils.connect()

connection = engine.connect()
result = connection.execute("select * from Movie")

for row in result:
    print("Title:", row['Title'])
connection.close()
