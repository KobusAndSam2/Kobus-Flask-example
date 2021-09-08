# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:59:15 2021

@author: jjpko
"""

from view.index import index_page
from view.images import image_page
from flask import current_app


def add_views():
    current_app.register_blueprint(index_page)
    current_app.register_blueprint(image_page)