import paho.mqtt.publish as mqtt
import time
import datetime
import json
import random
import user_info

server = "device.delicloud.com"
dqgzb_device = "3765C_21562167329C68E4"
dq_auth = {'username': '3765C',
           'password': '0A8E9F042864297FB6B02AB530494870'}
topic = "device"


def get_time():
    """获取当前时间戳"""
    now = int(time.time())
    # print(str(now))
    return now


def get_mid():
    """随机获得MID"""
    mid = "1582282748" + str(random.randint(000000000, 999999999))
    return mid


def syn_time():
    """生成同步时间代码"""
    msg = {"action": 100, "from": "3765C_21562167329C68E4",
           "mid": get_mid(), "time": get_time(), "to": "system"}
    msg_json = json.dumps(msg, separators=(',', ':'))
    return msg_json


def get_data(user_id):
    """构建签到data数据"""
    user_temp = {"check_time": get_time(), "check_type": "fp",
                 "user_id": user_id}
    user_temp1 = [user_temp]
    payload_temp = {"users": user_temp1}
    data = {"cmd": "checkin", "payload": payload_temp}

    return data


def check_in():
    """构建打卡消息数据"""
    msg = {}
    msg['action'] = 300
    msg['data'] = get_data(user_info.get_user())
    msg["from"] = "3765C_21562167329C68E4"
    msg["mid"] = get_mid()
    msg["time"] = get_time()
    msg["to"] = "377900597703081984"
    msg_json = json.dumps(msg, separators=(',', ':'))
    return msg_json


def quary_user(cell_phone):
    """通过手机号向服务器查询user_id"""
    # 该功能目前不可用
    cell_phone_1 = str(cell_phone)
    msg = {}
    msg['action'] = 517
    msg['data'] = {"region": "86", "mobile": cell_phone_1}
    msg["from"] = "3765C_21562167329C68E4"
    msg["mid"] = get_mid()
    msg["time"] = get_time()
    msg["to"] = "system"
    msg_json = json.dumps(msg, separators=(',', ':'))
    return msg_json


def go_publish(GongNeng):
    """执行消息发送"""
    mqtt.single(topic, payload=GongNeng, qos=1, retain=False, hostname=server, port=1883, client_id=dqgzb_device,
                keepalive=60, will=None, auth=dq_auth, tls=None, transport="tcp")



# go_publish(quary_user())
# print(quary_user())
