# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:04:55 2021

@author: jjpko
"""


from flask import Blueprint
from flask import current_app

index_page = Blueprint('Home_page', __name__)

@index_page.route('/home')
def index():
    current_app.celery.send_task('task.long_task', args=['test', 60])
    return 'hello world'