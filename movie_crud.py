from utils import connect, table
from sqlalchemy import MetaData, Table, select
from crud import search

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

    #movie = table('movie')

    select = '*'
    table = 'movie'
    filter = "title = {} and duration = {} and date = {}".format(title, duration, date)
    query = "select {} from {} where {}".format(select, table, filter)
    #query = "select {} from {}".format(select, table)
    #query = select([movie]).where(sqlalchemy.and(movie.columns.title == title, movie.columns.duration == duration, movie.columns.date == date))
    print(query)
    #filter = "title = {}, duration = {}, name = {}".format(title, duration, name)
    #query = "select {} from {} where {}".format('*', "movie")
    result = search(query)
    print(result)
