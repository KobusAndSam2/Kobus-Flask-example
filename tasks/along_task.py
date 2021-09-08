# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:12:28 2021

@author: jjpko
"""
import time

def long_task(filename, duration):
    for i in range(duration):
        with open(f'{filename}.txt', 'w+') as file:
            file.write(i.__str__())
        time.sleep(1)
            