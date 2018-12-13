# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Maxime Bourguignon and Christophe Simon

""" This script contains the useful functions. """

import yaml
from sqlalchemy import create_engine, MetaData, Table

def get(section, parameter):
    try:
        with open('config.yaml', 'r') as file:
            config = yaml.load(file)
        return config[section][parameter]
    except KeyError:
        return "{} introuvable dans {}".format(parametre, section)

def connect():
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

def table(str):
    engine = connect()

    meta = MetaData(engine)
    table = Table(str, meta, autoload=True)

    return table
