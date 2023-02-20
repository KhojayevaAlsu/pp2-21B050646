'''Write a Python program to print yesterday, today, tomorrow.'''

import datetime


today = datetime.datetime.today()
yesterday = datetime.datetime.today() - datetime.timedelta(1)
tomorrow = datetime.datetime.today() + datetime.timedelta(1)
print(today, yesterday, tomorrow)


'''
import datetime


today = datetime.datetime.today()
print(today.day - 1, today.day, today.day + 1)
'''
