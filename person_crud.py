from utils import connect
from sqlalchemy import MetaData, Table
from crud import search

def insert_person(firstname, lastname, birthdate, gender):
    try:
        engine = connect()

        meta = MetaData(engine)
        person = Table('person', meta, autoload=True)

        ins = person.insert().values(
        firstname=firstname,
        lastname=lastname,
        birthdate=birthdate,
        gender=gender)

        conn = engine.connect()
        conn.execute(ins)
        print("The person was successfully inserted.")

    except:
        print("ERROR: the person was not successfully inserted.")

def search_person(firstname, lastname, birthdate, gender):

    select = '*'
    table = 'person'
    filter = "firstname = {} and lastname = {} and birthdate = {} and gender = {}".format(firstname, lastname, birthdate, gender)
    query = "select {} from {} where {}".format(select, table, filter)

    print(query)

    result = search(query)
    preint(result)
