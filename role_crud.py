from utils import connect
from sqlalchemy import MetaData, Table
from crud import search

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

    select = '*'
    table = 'role'
    filter = "name = {}".format(name)
    query = "select {} from {} where {}".format(select, table, filter)

    print(query)

    result = search(query)
    print(result)
