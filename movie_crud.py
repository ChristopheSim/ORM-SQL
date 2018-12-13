import utils
from datetime import date
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy.ext.automap import automap_base

def insert_movie(title, duration, date):
    try:
        engine = utils.connect()

        meta = MetaData(engine)
        movie = Table('movie', meta, autoload=True)

        ins = movie.insert().values(
        date=date,
        duration=duration,
        title=title)

        conn = engine.connect()
        conn.execute(ins)

    except:
        print("An error occured during the insertion of a movie.")
"""
# insert multiple data
conn.execute(movie.insert(),[
   {'date':date(2018, 12, 11),'time':120, 'title':'Test2'},
   {'date':date(2018, 12, 11),'time':120, 'title':'Test3'}])
 """
