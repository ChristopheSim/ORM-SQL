# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Maxime Bourguignon and Christophe Simon

from utils import connect

def search(query):
    try:
        engine = connect()

        result = engine.execute(query)
        return result.fetchall()

    except:
        print("An error occured during the search of a movie.")
