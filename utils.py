# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Maxime Bourguignon and Christophe Simon

""" This script contains the useful functions. """

import yaml
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import Column, ForeignKey, inspect
from sqlalchemy import Integer, String, Date
from sqlalchemy_utils import functions, database_exists, create_database
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base



def get(section, parameter):
    try:
        with open('config.yaml', 'r') as file:
            config = yaml.load(file)
        return config[section][parameter]
    except KeyError:
        return "{} introuvable dans {}".format(parameter, section)



def connect():
    try:
        username = get("db", "login")
        password = get("db", "password")
        port = get("db", "port")
        database = get("db", "name")
        url = get("db", "url")

        engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(username,
                                                                password,
                                                                url,
                                                                port,
                                                                database),
                                echo=True)
        return engine
    except:
        print("ERROR: no connection to the database.")



def drop_db():
    try:
        engine = connect()

        if database_exists(engine.url):
            functions.drop_database(engine.url)
            print("The database was successfully dropped.")
    except:
        print("ERROR: the database was not successfully dropped.")
