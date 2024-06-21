# login.py

import json

logged_in_user = None  # 초기에 로그인 사용자를 None으로 설정

def login_user(username, password):
    global logged_in_user

    users = load_users()
    if username in users and users[username] == password:
        logged_in_user = username  # 로그인한 사용자를 전역 변수에 저장
        return True
    else:
        logged_in_user = None  # 로그인 실패 시 None으로 설정
        return False

def is_logged_in():
    return logged_in_user is not None

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

