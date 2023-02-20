'''Write a Python program to drop microseconds from datetime.'''

import datetime


today = datetime.datetime.today()
print(today.strftime('%x %X'))