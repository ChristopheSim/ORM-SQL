from sqlalchemy import create_engine
import utils

engine = utils.connect()

connection = engine.connect()
result = connection.execute("select * from movie")

for row in result:
    print("Title:", row['Title'])
connection.close()
