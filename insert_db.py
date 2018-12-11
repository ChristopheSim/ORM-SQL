import utils
from datetime import date
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy.ext.automap import automap_base

engine = utils.connect()

# insert data via insert() construct in movies
meta = MetaData(engine)

movie = Table('movie', meta, autoload=True)

ins = movie.insert().values(
      date=date(2018, 12, 11),
      time=120,
      title='Test1')
conn = engine.connect()
conn.execute(ins)

# insert multiple data
conn.execute(movie.insert(),[
   {'date':date(2018, 12, 11),'time':120, 'title':'Test2'},
   {'date':date(2018, 12, 11),'time':120, 'title':'Test3'}])
