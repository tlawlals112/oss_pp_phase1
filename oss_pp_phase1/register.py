# register.py

import json

def register_user(username, password):
    users = load_users()
    if username in users:
        print("이미 존재하는 사용자 이름입니다.")
        return False
    users[username] = password
    save_users(users)
    print("회원가입이 완료되었습니다.")
    return True

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

