import datetime
from chinese_calendar import is_workday, is_holiday
import random
import time
#is_workday(april_last)

"""
start = input ("请输入开始日期：")
end = input("请输入结束日期：")
 
datestart = datetime.datetime.strptime(start, '%Y.%m.%d')
dateend = datetime.datetime.strptime(end, '%Y.%m.%d')
workday = [] 
dalta= datetime.timedelta(days=1) 
while datestart <= dateend:
    if is_workday(datestart):
        h = 8
        m = random.randint(45, 59)
        s = random.randint(00, 59)
        datestart = datestart.replace(hour = h,minute = m,second = s)
        print (datestart)
        workday.append(datestart)
    datestart += dalta
print (workday)   

tt = "2020.5.1"
tt = datetime.datetime.strptime(tt,'%Y.%m.%d')
print (tt)
h = 8
tt = tt.replace(hour = h)
print (tt)
"""

def get_workday(start,end):
    start = datetime.datetime.strptime(start, '%Y.%m.%d')
    end = datetime.datetime.strptime(end, '%Y.%m.%d')
    workday = []
    while start <= end:
        if is_workday(start):
            h = 8
            m = random.randint(45, 59)
            s = random.randint(00, 59)
            start = start.replace(hour = h,minute = m,second = s)
            print(start)
            tt = time.strptime(str(start),"%Y-%m-%d %H:%M:%S")
            time_stamp = int(time.mktime(tt))
            workday.append(time_stamp)
            print(time_stamp)
        start += datetime.timedelta(days=1)
    print(workday)
    return workday

get_workday('2020.4.10','2020.4.18')
