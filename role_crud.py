from utils import connect
from sqlalchemy import MetaData, Table

def insert_role(name):
    try:
        engine = connect()

        meta = MetaData(engine)
        role = Table('role', meta, autoload=True)

        ins = role.insert().values(
        name=name)

        conn = engine.connect()
        conn.execute(ins)
        print("The role was successfully inserted.")

    except:
        print("ERROR: the role was not successfully inserted.")
