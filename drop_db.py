# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Maxime Bourguignon and Christophe Simon

import utils
from sqlalchemy_utils import functions

if __name__ == "__main__":
    engine = utils.connect()

    if functions.database_exists(engine.url):
        functions.drop_database(engine.url)

    print("db dropped")
