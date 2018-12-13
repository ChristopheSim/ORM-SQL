from utils import table
from sqlalchemy import MetaData, Table, select

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

    except:
        print("An error occured during the insertion of a movie.")
"""
# insert multiple data
conn.execute(movie.insert(),[
   {'date':date(2018, 12, 11),'time':120, 'title':'Test2'},
   {'date':date(2018, 12, 11),'time':120, 'title':'Test3'}])
 """

def search(query):
    try:
        engine = connect()

        result = engine.execute(query)
        return result

    except:
        print("An error occured during the search of a movie.")

def search_movie(title, duration, name):

    movie = table('movie')

    query = select([movie])
    print(query)
    #filter = "title = {}, duration = {}, name = {}".format(title, duration, name)
    #query = "select {} from {} where {}".format('*', "movie")
    result = search(query)
    print(result)
