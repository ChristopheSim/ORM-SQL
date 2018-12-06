from sqlalchemy import create_engine

username = "chris"
password = "root"
port = 3306
database = "movies"

engine = create_engine('mysql://{}:{}@localhost:{}/{}'.format(username,
                                                              password,
                                                              port,
                                                              database),
                       echo=True)

connection = engine.connect()
result = connection.execute("")
