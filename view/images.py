# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:23:01 2021

@author: jjpko
"""

import os
from flask import Blueprint
from flask import send_from_directory
from flask import current_app

image_page = Blueprint('image_page', __name__)

@image_page.route('/images/<image_name>.png')
def image(image_name):
    filedirectory = os.path.abspath('Static')
    print(filedirectory)
    filename = f'{image_name}.png'
    return send_from_directory(filedirectory, filename)