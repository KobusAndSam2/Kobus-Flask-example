# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:02:44 2021

@author: jjpko
"""

from celery import shared_task
from tasks.along_task import long_task

@shared_task(name = 'task.long_task')
def cel_long_task(filename, duration):
    return long_task(filename, duration)
