# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:52:13 2021

@author: jjpko
"""

from celery import Celery

# Celery Configuration
def make_celery( app ):
    celery = Celery('flask-celery',
                    backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'],
                    include=['tasks.app_tasks'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery