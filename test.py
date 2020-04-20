import datetime
from chinese_calendar import is_workday, is_holiday
import random
import time
import json
# is_workday(april_last)

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

# msg = {"action": 300, "data": {"cmd": "checkin", "payload": {"users": [{"check_time": 1587115138, "check_type": "fp", "user_id": "598529995907792896"}]}},
#        "to": "377900597703081984", "time": 1587115138, "from": "3765C_21562167329C68E4", "mid": "1582282748929186295"}
# tt = msg.get('time')
# print (tt)


def get_workday(start, end):
    start = datetime.datetime.strptime(start, '%Y.%m.%d')
    end = datetime.datetime.strptime(end, '%Y.%m.%d')
    workday = []
    while start <= end:
        if is_workday(start):
            h = 8
            m = random.randint(45, 59)
            s = random.randint(00, 59)
            start = start.replace(hour=h, minute=m, second=s)
            tt = time.strptime(str(start), "%Y-%m-%d %H:%M:%S")
            time_stamp = int(time.mktime(tt))
            workday.append(time_stamp)
            h = 17
            m = random.randint(00, 30)
            s = random.randint(00, 59)
            start = start.replace(hour=h, minute=m, second=s)
            tt = time.strptime(str(start), "%Y-%m-%d %H:%M:%S")
            time_stamp = int(time.mktime(tt))
            workday.append(time_stamp)
        start += datetime.timedelta(days=1)
    return workday


def make_checkin(user_id, ck_time):
    """构建签到data数据"""
    if ck_time == "now":
        time = get_now_time()
    elif ck_time == "re_ck":
        time = get_time_ver()
    else:
        time = ck_time
    user_temp = {"check_time": time, "check_type": "fp",
                 "user_id": user_id}
    user_temp1 = [user_temp]
    payload_temp = {"users": user_temp1}
    data = {"cmd": "checkin", "payload": payload_temp}
    return data


def circle_checkin(start_date, end_date, user_id):
    """执行循环补打操作"""
    workday_arry = get_workday(start_date, end_date)
    msg = {}
    c_data = []
    for i in workday_arry:
        c_checkin = make_checkin(user_id, i)
        msg['action'] = 300
        msg['data'] = c_checkin
        msg["to"] = "377900597703081984"
        msg["time"] = msg['data']['payload']['users'][0]['check_time']
        msg["from"] = "3765C_21562167329C68E4"
        # msg["mid"] = get_mid()
        msg_json = json.dumps(msg, separators=(',', ':'))
        c_data.append(msg_json)
        # print (c_data)

    for i in c_data:
        mmsg = json.loads(i)
        mmmsg = mmsg["time"]
        cf_cktime = datetime.datetime.fromtimestamp(mmmsg)
        print(cf_cktime)
    return c_data
    # for mm in c_data:
    #    go_publish(mm)


circle_checkin('2020.4.10', '2020.4.18', '598529995907792896')


