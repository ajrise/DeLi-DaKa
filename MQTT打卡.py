import paho.mqtt.publish as mqtt
import time
import datetime
import json
import random
import user_info
import sys
from chinese_calendar import is_workday


server = "device.delicloud.com"
dqgzb_device = "3765C_21562167329C68E4"
dq_auth = {'username': '3765C',
           'password': '0A8E9F042864297FB6B02AB530494870'}
topic = "device"


def get_now_time():
    """获取当前时间戳"""
    time_now = round(time.time())
    # print(str(now))
    return time_now


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


def get_time_ver():
    """生成补卡时间"""
    while True:
        time_ver = input("1：补打今日上班卡    2：补打今日下班卡    D：指定补卡日期时间 \n请输入补卡时间：")
        if time_ver == "1":
            t = datetime.date.today()
            h = 8
            m = random.randint(45, 59)
            s = random.randint(00, 59)
            dt = str(t) + " " + str(h) + ":" + str(m) + ":" + str(s)
            time_str = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
            time_stamp = int(time.mktime(time_str))
            return time_stamp
            break
        elif time_ver == "2":
            t = datetime.date.today()
            h = 17
            m = random.randint(00, 30)
            s = random.randint(00, 59)
            dt = str(t) + " " + str(h) + ":" + str(m) + ":" + str(s)
            time_str = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
            time_stamp = int(time.mktime(time_str))
            return time_stamp
            break
        elif time_ver == "d" or time_ver == "D":
            time_ver = input("指定日期合时间的格式为：YY.MM.DD HH.MM.SS \n 请输入要补卡的日期和时间： ")
            time_str = time.strptime(time_ver, "%Y.%m.%d %H.%M.%S")
            time_stamp = int(time.mktime(time_str))
            return time_stamp
            break
        else:
            print("输入错误，请重新输入！")
            continue


def get_mid():
    """随机获得MID"""
    mid = "1582282748" + str(random.randint(000000000, 999999999))
    return mid


def make_time_syn():
    """生成同步时间代码"""
    msg = {"action": 100, "from": "3765C_21562167329C68E4",
           "mid": get_mid(), "time": get_now_time(), "to": "system"}
    msg_json = json.dumps(msg, separators=(',', ':'))
    return msg_json


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


def make_msg(fun_id):
    """构建消息payload数据"""
    msg = {}
    if fun_id == "check_in":
        msg['action'] = 300
        msg['data'] = make_checkin(user_info.get_user(), "now")
        msg["to"] = "377900597703081984"
        msg["time"] = get_now_time()
    elif fun_id == "time_syn":
        msg['action'] = 100
        msg["to"] = "system"
        msg["time"] = get_now_time()
    elif fun_id == "re_check_in":
        msg['action'] = 300
        msg['data'] = make_checkin(user_info.get_user(), "re_ck")
        msg["to"] = "377900597703081984"
        msg["time"] = msg['data']['payload']['users'][0]['check_time']

    msg["from"] = "3765C_21562167329C68E4"
    msg["mid"] = get_mid()
    msg_json = json.dumps(msg, separators=(',', ':'))
    return msg_json


def go_publish(GongNeng):
    """执行消息发送"""
    mqtt.single(topic, payload=GongNeng, qos=1, retain=False, hostname=server, port=1883, client_id=dqgzb_device,
                keepalive=60, will=None, auth=dq_auth, tls=None, transport="tcp")
    cf_cktime = datetime.datetime.fromtimestamp(GongNeng['time'])
    print(str(cf_cktime) + "  操作已成功!")


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
        msg["mid"] = get_mid()
        msg_json = json.dumps(msg, separators=(',', ':'))
        c_data.append(msg_json)
    for mm in c_data:
        go_publish(mm)


def time_syn():
    msgg = make_msg("time_syn")
    print(msgg)
    go_publish(msgg)


def check_in():
    msg = make_msg("check_in")
    go_publish(msg)


def main():
    while True:
        welcome_title = "请选择需要进行的操作：\n 1、同步时间（确定系统状态）   2、立即打卡     3、补打卡   0、批量补打卡   Q、退出     \n 请输入："
        fun_select = input(welcome_title)
        if fun_select == "1":
            time_syn()
        elif fun_select == "2":
            check_in()
        elif fun_select == "3":
            msg = make_msg("re_check_in")
            go_publish(msg)
        elif fun_select == "0":
            start_date = input("请输入补打起始日期：")
            end_date = input("请输入结束日期：")
            circle_checkin(start_date, end_date, user_info.get_user())
        elif fun_select == "q" or fun_select == "Q":
            sys.exit()

        else:
            print("---------------------输入错误，请重新输入！----------------------")


main()
#print (make_msg("time_syn"))
#print (make_msg("check_in"))
#print (make_msg("re_check_in"))
# go_publish(quary_user())
# print(quary_user())
#print (get_time_ver())
