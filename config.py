import pytest

base_url = "http://192.168.115.130:8080"
Authorization = ""
Authorizationnew = ""

USERNAME = "aiops"
PASSWORD = "aiops@2019"
service_id = ""
module_id = ""  # 模块id
event_id = ""  # 事件id


def pprint(url, jobs, data=""):
    print("【请求URL】：")
    print(url)
    if data != "":
        print("【请求参数】：")
        print(data)
    print("【返回结果】：")
    print(jobs)
