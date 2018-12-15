from utils import connect
from sqlalchemy import MetaData, Table
from crud import search
from create_db2 import Base, Link
from sqlalchemy.orm import sessionmaker

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

    engine = connect()
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()

    result = session.query(Link).filter(Link.fk_movie == fk_movie).filter(Link.fk_person == fk_person).filter(Link.fk_role == fk_role).all()
    print(result)
    print(len(result))
    for r in result:
        print((r.pk_link, r.fk_movie, r.fk_person, r.fk_role))
