# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:57:54 2021

@author: jjpko
https://stackoverflow.com/questions/59632556/importing-celery-in-flask-blueprints
"""

from celery import Celery

# Celery Configuration
def make_celery():
    celery = Celery('flask-celery',
                    backend='redis://localhost:6379',
                    broker='redis://localhost:6379',
                    include=['tasks.app_tasks'])
    return celery

celery = make_celery()
print("tasks={}".format( celery.tasks.keys() ))