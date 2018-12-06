# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Maxime Bourguignon and Christophe Simon

""" This script contains the useful functions. """

import yaml



def get(section, parameter):
    try:
        with open('config.yaml', 'r') as file:
            config = yaml.load(file)
        return config[section][parameter]
    except KeyError:
        return "{} introuvable dans {}".format(parametre, section)
