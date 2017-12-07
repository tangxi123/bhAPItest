# -*- coding:utf-8 -*-
import requests
import json
def login():
    login_url = "http://bhtest.51s.co/vc/system/user/session"
    login_info = '{"mobile":"11111111111","password":"123456"}'
    s = requests.Session()
    r = s.post(login_url, login_info)
    return s

if __name__ == "__main__":
    login()