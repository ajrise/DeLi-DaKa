import json


def load_user():
    with open("user.json") as user_obj:
        user_db = json.load(user_obj)
        user_obj.close()
        return user_db


def add_user(new_user, new_user_id):
    user_db = load_user()
    new = {new_user: new_user_id}
    user_db.update(new)
    with open ("user.json",'w') as user_obj:
        user_obj.write(json.dumps(user_db))
        user_obj.close()
    print (user_db)


def get_id():

    """user_name_input = input("请输入用户名：")

    if user_name_input in user_db:
        user_id = user_db.get(user_name_input)
        return user_id

    else:
        if input("用户不存在！是否新建用户？y/n：") == "y":
            new_user_id1 = input("请输入“"+user_name_input+"”的ID：")
            add_user(user_name_input, new_user_id1)
        else:
            return "quit"
"""
    user_id = "598529995907792896"
    return user_id

# def get_user(id):
#     user_db = load_user()
#     username = user_db.get(id)
#     return username
# print(get_user('598529995907792896'))

def find_id(input):
    


def last_login(fun_id):
    user_db = load_user()
    if fun_id == 0:
        last_login = user_db.get('last_login')
    elif fun_id == 1:
        with open ("user.json",'w') as user_obj:
            user_db['last_login'] = ''
            user_obj.write(json.dumps(user_db))
            user_obj.close()
    return last_login