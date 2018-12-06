from sqlakchemy_utils import functions
from utils import get

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

if functions.database_exists(engine.database):
    drop_database(engine.database)

if __name__ == "__main__":
    print("Drop db")
