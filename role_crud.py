# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Maxime Bourguignon and Christophe Simon

from utils import connect
from sqlalchemy import MetaData, Table
from create_db import Base, Role
from sqlalchemy.orm import sessionmaker



def insert_role(name):
    try:
        engine = connect()

        meta = MetaData(engine)
        role = Table('role', meta, autoload=True)

        ins = role.insert().values(
        name=name)

        conn = engine.connect()
        conn.execute(ins)
        print("The role was successfully inserted.")

    except:
        print("ERROR: the role was not successfully inserted.")



def search_role(pk_role=False, name=False):
    try:
        engine = connect()
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        if name:
            result = session.query(Role).filter(Role.name == name).all()
        elif pk_role:
            result = session.query(Role).filter(Role.pk_role == pk_role).all()
        else:
            result = session.query(Role).all()
        
        print(result)
        print(len(result))
        for r in result:
            print((r.pk_role, r.name))
        return result
    except:
        print("ERROR: no role found.")



def update_role(id, name):
    try:
        engine = connect()
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        result = session.query(Role).filter(Role.pk_role == id).\
        update({"name": name}, synchronize_session=False)
        session.commit()
        if result is not None:
            print("The role was successfully updated.")
        else:
            print("The role was not successfully updated.")
    except:
        print("ERROR: no role updated.")



def delete_role(id):
    try:
        engine = connect()
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        result = session.query(Role).filter(Role.pk_role == id).\
        delete(synchronize_session=False)
        session.commit()
        if result is not None:
            print("The role was successfully deleted.")
        else:
            print("The role was not successfully deleted.")
    except:
        print("ERROR: no role deleted.")
