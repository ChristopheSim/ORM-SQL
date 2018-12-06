from sqlalchemy import create_engine
from utils.py import utils

username = get("db", "login") 
password = get("db", "password")
port = get("db", "port")
database = get("db", "name")
url = get("db", "url")


engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(username,
                                                        password,
                                                        url,
                                                        port,
                                                        database),
                       echo=True)

connection = engine.connect()
result = connection.execute("select * from Movie")

for row in result:
    print("Title:", row['Title'])
connection.close()
