# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Maxime Bourguignon and Christophe Simon

from utils import connect
from sqlalchemy import MetaData, Table
from crud import search
from create_db2 import Base, Person
from sqlalchemy.orm import sessionmaker



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
    try:
        engine = connect()
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        result = session.query(Person).filter(Person.firstname == firstname).\
        filter(Person.lastname == lastname).\
        filter(Person.birthdate == birthdate).filter(Person.gender == gender).\
        all()
        print(result)
        print(len(result))
        for r in result:
            print((r.pk_person, r.firstname, r.lastname, r.birthdate,
            r.gender))
    except:
        print("ERROR: no person found.")



def update_person(id, firstname, lastname, birthdate, gender):
    try:
        engine = connect()
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        result = session.query(Person).filter(Person.pk_person == id).\
        update({"firstname": firstname, "lastname": lastname,
        "birthdate": birthdate, "gender": gender}, synchronize_session=False)
        session.commit()
        if result is not None:
            print("The person was successfully updated.")
        else:
            print("The person was not successfully updated.")
    except:
        print("ERROR: no person updated.")



def delete_person(id):
    try:
        engine = connect()
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        result = session.query(Person).filter(Person.pk_person == id).\
        delete(synchronize_session=False)
        session.commit()
        if result is not None:
            print("The person was successfully deleted.")
        else:
            print("The person was not successfully deleted.")
    except:
        print("ERROR: no person deleted.")
