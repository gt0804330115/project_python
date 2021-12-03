import time

localtime = time.localtime(time.time())
print("本地时间：", localtime)

import time

localtime = time.asctime(time.localtime(time.time()))
print("本地时间：", localtime)

import calendar

cal = calendar.month(2020,11)
print(cal)
