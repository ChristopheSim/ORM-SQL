from utils import connect
from sqlalchemy import MetaData, Table

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
