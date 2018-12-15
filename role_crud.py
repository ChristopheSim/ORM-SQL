from utils import connect
from sqlalchemy import MetaData, Table
from crud import search
from create_db2 import Base, Role
from sqlalchemy.orm import sessionmaker

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


def search_role(name):

    engine = connect()
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()

    result = session.query(Role).filter(Role.name == name).all()
    print(result)
    print(len(result))
    for r in result:
        print((r.pk_role, r.name))
