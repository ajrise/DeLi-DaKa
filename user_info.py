import json


def load_user():
    with open("user.json") as user_obj:
        user_db = json.load(user_obj)
        user_obj.close()
        return user_db


def add_user(new_user, new_user_id):
    user_db = load_user()
    new = {new_user: new_user_id}
    print(new)
    user_db.update(new)


def get_user():
    user_db = load_user()
    user_name_input = input("请输入用户名：")

    if user_name_input in user_db:
        user_id = user_db.get(user_name_input)
        print(str(user_id))
        return user_id
    else:
        if input("用户不存在！是否新建用户？y/n") == "y":
            new_user_id1 = input("请输入“"+user_name_input+"”的ID：")
            add_user(user_name_input, new_user_id1)
        else:
            return "quit"


get_user()
# print(load_user())
