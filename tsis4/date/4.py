'''Write a Python program to calculate two date difference in seconds.'''

import datetime


datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
date1 = '2020-04-16 10:01:28.585'
date2 = '2023-03-10 08:56:28.067'
diff = datetime.datetime.strptime(date1, datetimeFormat)- datetime.datetime.strptime(date2, datetimeFormat)
 

print(diff.seconds)