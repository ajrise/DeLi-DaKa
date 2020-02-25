import paho.mqtt.publish as mqtt
import time
import datetime
import json
import random
import user_info
import sys

server = "device.delicloud.com"
dqgzb_device = "3765C_21562167329C68E4"
dq_auth = {'username': '3765C',
           'password': '0A8E9F042864297FB6B02AB530494870'}
topic = "device"


def get_now_time():
    """获取当前时间戳"""
    time_now = int(time.time())
    # print(str(now))
    return time_now


def get_time_ver():
    """生成补卡时间"""
    time_ver = input("请输入补卡时间：")
    time_str = time.strptime(time_ver, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(time_str))
    return time_stamp


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
    user_temp = {"check_time": time, "check_type": "fp",
                 "user_id": user_id}
    user_temp1 = [user_temp]
    payload_temp = {"users": user_temp1}
    data = {"cmd": "checkin", "payload": payload_temp}
    return data


def make_msg(fun_id):
    """构建消息data数据"""
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


def quary_user(cell_phone):
    """通过手机号向服务器查询user_id"""
    # 该功能目前不可用
    cell_phone_1 = str(cell_phone)
    msg = {}
    msg["mid"] = get_mid()
    msg["from"] = "3765C_21562167329C68E4"
    msg["to"] = "system"
    msg["time"] = get_now_time()
    msg['action'] = 517
    msg['data'] = {"region": "86", "mobile": cell_phone_1}
    msg_json = json.dumps(msg, separators=(',', ':'))
    return msg_json


def go_publish(GongNeng):
    """执行消息发送"""
    mqtt.single(topic, payload=GongNeng, qos=1, retain=False, hostname=server, port=1883, client_id=dqgzb_device,
                keepalive=60, will=None, auth=dq_auth, tls=None, transport="tcp")
    print("操作已成功!")


while True:
    welcome_title = "请选择需要进行的操作：\n 1、同步时间（确定系统状态）   2、立即打卡     3、补打卡   Q、退出     \n 请输入："
    fun_select = input(welcome_title)
    if fun_select == "1":
        go_publish(make_msg("time_syn"))
    elif fun_select == "2":
        go_publish(make_msg("check_in"))
    elif fun_select == "3":
        go_publish(make_msg("re_check_in"))
    elif fun_select == "q" or "Q":
        sys.exit()
    else :
        print("输入错误，请重新输入！")


#print (make_msg("time_syn"))
#print (make_msg("check_in"))
#print (make_msg("re_check_in"))
# go_publish(quary_user())
# print(quary_user())
#print (get_time_ver())