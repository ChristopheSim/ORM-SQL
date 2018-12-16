# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Maxime Bourguignon and Christophe Simon

from utils import connect, table
from sqlalchemy import MetaData, Table, select
from sqlalchemy.orm import sessionmaker
from crud import search
from create_db2 import Movie, Base

# source : https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/

def insert_movie(title, duration, date):
    try:
        engine = connect()

        meta = MetaData(engine)
        movie = Table('movie', meta, autoload=True)

        ins = movie.insert().values(
        date=date,
        duration=duration,
        title=title)

        conn = engine.connect()
        conn.execute(ins)
        print("The movie was successfully inserted.")

    except:
        print("ERROR: the movie was not successfully inserted.")

"""
# insert multiple data
conn.execute(movie.insert(),[
   {'date':date(2018, 12, 11),'time':120, 'title':'Test2'},
   {'date':date(2018, 12, 11),'time':120, 'title':'Test3'}])
 """

def search_movie(title, duration, date):
    try:
        engine = connect()
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        result = session.query(Movie).filter(Movie.title == title).filter(Movie.duration == duration).filter(Movie.date == date).all()
        print(result)
        print(len(result))
        for r in result:
            print((r.pk_movie, r.title, r.duration, r.date))
    except:
        print("ERROR: no movie found.")


def update_movie(id, title, duration, date):
    try:
        engine = connect()
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        result = session.query(Movie).filter(Movie.pk_movie == id).\
        update({"title": title, "duration": duration,
        "date": date}, synchronize_session=False)
        session.commit()
        if result is not None:
            print("The movie was successfully updated.")
        else:
            print("The movie was not successfully updated.")
    except:
        print("ERROR: no movie updated.")


def delete_movie(id):
    try:
        engine = connect()
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        result = session.query(Movie).filter(Movie.pk_movie == id).\
        delete(synchronize_session=False)
        session.commit()
        if result is not None:
            print("The movie was successfully deleted.")
        else:
            print("The movie was not successfully deleted.")
    except:
        print("ERROR: no movie deleted.")
