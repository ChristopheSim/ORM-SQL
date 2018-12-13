from utils import connect

def search(query):
    try:
        engine = connect()

        result = engine.execute(query)
        return result.fetchall()

    except:
        print("An error occured during the search of a movie.")
