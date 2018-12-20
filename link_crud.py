# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Maxime Bourguignon and Christophe Simon

from utils import connect
from sqlalchemy import MetaData, Table
from create_db import Base, Link
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



def search_link(fk_movie=False, fk_person=False, fk_role=False):
    try:
        engine = connect()
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        if fk_movie and fk_person and fk_role:
            result = session.query(Link).filter(Link.fk_movie == fk_movie).filter(Link.fk_person == fk_person).filter(Link.fk_role == fk_role).all()
        elif fk_movie and fk_person:
            result = session.query(Link).filter(Link.fk_movie == fk_movie).filter(Link.fk_person == fk_person).all()
        elif fk_movie and fk_role:
            result = session.query(Link).filter(Link.fk_movie == fk_movie).filter(Link.fk_role == fk_role).all()
        elif fk_person and fk_role:
            result = session.query(Link).filter(Link.fk_person == fk_person).filter(Link.fk_role == fk_role).all()
        else:
            result = sessionquery(Link).all()
        print(result)
        print(len(result))
        for r in result:
            print((r.pk_link, r.fk_movie, r.fk_person, r.fk_role))
    except:
        print("ERROR: no link found.")



def update_link(id, fk_movie, fk_person, fk_role):
    try:
        engine = connect()
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        result = session.query(Link).filter(Link.pk_link == id).\
        update({"fk_movie": fk_movie, "fk_person": fk_person,
        "fk_role": fk_role}, synchronize_session=False)
        session.commit()
        if result is not None:
            print("The link was successfully updated.")
        else:
            print("The link was not successfully updated.")
    except:
        print("ERROR: no link updated.")



def delete_link(id):
    try:
        engine = connect()
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        result = session.query(Link).filter(Link.pk_link == id).\
        delete(synchronize_session=False)
        session.commit()
        if result is not None:
            print("The link was successfully deleted.")
        else:
            print("The link was not successfully deleted.")
    except:
        print("ERROR: no link deleted.")
