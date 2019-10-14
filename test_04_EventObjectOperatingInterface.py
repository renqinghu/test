import requests
import pytest
import config
import json
import time
import math


class TestEventInterface(object):
    """
    Test get a list of jobs from jenkins
    """
    node_key = "node.bztest001"
    modigynode_key = "node.bztest002"
    name = "rqhtest007"

    def test_01_getapievent(self):
        '''获取事件列表[get] /api/event'''
        url = config.base_url + "/api/event"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        print(jobs["data"][0]["service_id"])

        config.service_id = jobs["data"][0]["service_id"]

    def test_02_postapievent(self):
        '''创建事件[post] /api/event'''
        url = config.base_url + "/api/event"
        headers = {'Content-Type': 'application/json'}
        print(config.service_id)
        data = {
            "service_id": config.service_id,
            "type": "custom",
            "time": int(time.time()),
            "finish": False,
            "update_time": 1536822741,
            "description": "rqhtest业务更新定时分析",
            "anomaly_kpi": [
                {
                    "kpi_key": "kpi.mobilebank.trans_volume",
                    "kpi_name": "rqhtest手机银行交易量",
                    "description": "300秒内出现12个异常点"
                }
            ],
            "analysis": ["fluxrank"]
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs,data)
        assert jobs["code"] == 201
        assert jobs["msg"] == "Created"
        assert jobs["data"]["service_id"] == config.service_id
        config.event_id = jobs["data"]["event_id"]

    def test_02_getapievent(self):
        '''获取事件列表[get] /api/event'''
        url = config.base_url + "/api/event"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert r.text.count("rqhtest业务更新定时分析") >= 1

    def test_03_getapievent_id(self):
        '''获取事件对象[get] /api/event/:event_id'''
        url = config.base_url + "/api/event/" + config.event_id
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert jobs["data"]["event_id"] == config.event_id

    def test_04_postapievent_id(self):
        '''更新事件[post] /api/event/:event_id'''
        url = config.base_url + "/api/event/" + config.event_id
        headers = {'Content-Type': 'application/json'}
        data = {
            "description": "交易量出现异常",
            "update_time": int(time.time()),
            "finish": False,
            "anomaly_kpi": [
                {
                    "kpi_key": "kpi.mobilebank.trans_volume",
                    "kpi_name": "手机银行交易量",
                    "description": "500秒内出现20个异常点"
                }
            ],
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_05_deleteapievent_id(self):
        '''删除事件[delete] /api/event/:event_id'''
        url = config.base_url + "/api/event/" + config.event_id
        headers = {'Content-Type': 'application/json'}

        r = requests.delete(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_06_getapievent(self):
        '''获取事件列表[get] /api/event'''
        url = config.base_url + "/api/event"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert r.text.count("rqhtest业务更新定时分析") >= 0

    def test_06_putapievent_id(self):
        '''提交事件多维根因分析结果[put] /api/event/:event_id/fluxrank'''
        url = config.base_url + "/api/event/" + config.event_id + "/fluxrank"
        headers = {'Content-Type': 'application/json'}
        data = {
            "description": "交易量出现异常",
            "update_time": int(time.time()),
            "finish": False,
            "anomaly_kpi": [
                {
                    "kpi_key": "kpi.mobilebank.trans_volume",
                    "kpi_name": "手机银行交易量",
                    "description": "500秒内出现20个异常点"
                }
            ],
        }
        r = requests.put(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs,data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
