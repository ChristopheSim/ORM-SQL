from utils import connect
from sqlalchemy import MetaData, Table

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
