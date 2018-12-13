from utils import connect
from sqlalchemy import MetaData, Table
from crud import search

def insert_link(fk_movie, fk_person, fk_role):
    try:
        engine = connect()

        meta = MetaData(engine)
        link = Table('link', meta, autoload=True)

        ins = link.insert().values(
        fk_movie=fk_movie,
        fk_person=fk_person,
        fk_role=fk_role)

        conn = engine.connect()
        conn.execute(ins)
        print("The link was successfully inserted.")

    except:
        print("ERROR: the link was not successfully inserted.")

def search_link(fk_movie, fk_person, fk_role):

    select = '*'
    table = 'link'
    filter = "fk_movie = {} and fk_person = {} and fk_role = {}".format(fk_movie, fk_person, fk_role)
    query = "select {} from {} where {}".format(select, table, filter)

    print(query)

    result = search(query)
    print(result)
