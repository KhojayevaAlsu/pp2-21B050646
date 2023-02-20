'''Write a Python program to subtract five days from current date.'''

import datetime


days = 5
new_date = datetime.datetime.today() - datetime.timedelta(days)
print(new_date)


'''
import datetime

today = datetime.datetime.today()
print(today.day - 5)
'''