import requests
import pytest
import config
import json
import time
from test_scene import test_01_BM_new_business


class TestNewBusiness(object):
    """
    业务监控--【新建业务 -> 新建告警 -> 业务概览查询 -> 告警列表查询 -> 查看 -> 删除】
    """
    node_key = "node.bztest001"
    modigynode_key = "node.bztest002"
    name = "rqh_test"
    eventdesc = "测试新建告警事件"

    def test_01_postservice(self):
        '''新建业务--新建告警事件'''
        # test_01_BM_new_business.TestNewBusiness().test_01_postservice()

        url = config.base_url + "/api/event"
        headers = {'Content-Type': 'application/json'}
        data = {"service_id": config.service_id, "type": "custom", "time": int(time.time()),
                "description": self.eventdesc,
                "anomaly_kpi": [], "analysis": ["fluxrank"]}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 201
        assert jobs["msg"] == "Created"
        assert len(jobs["data"]) != 0
        config.event_id = jobs["data"]["event_id"]

    def test_02_geteventid(self):
        '''查询告警事件'''
        url = config.base_url + "/api/event/" + config.event_id
        headers = {'Content-Type': 'application/json'}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_03_getevent(self):
        '''在告警列表中 查询告警事件'''
        url = config.base_url + "/api/event?services=" + config.service_id + "&duration=" + str(
            int(time.time() - 1000000)) + "," + str(
            int(time.time()))
        headers = {'Content-Type': 'application/json'}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        assert jobs["data"][0]["event_id"] == config.event_id
        assert jobs["data"][0]["service_id"] == config.service_id
        assert jobs["data"][0]["description"] == self.eventdesc
        # assert jobs["data"][0]["service_name"] == test_01_BM_new_business.TestNewBusiness.name

    def test_04_getmodules(self):
        '''在告警列表中 --查询告警事件 - 点击查看按钮'''
        url = config.base_url + "/api/service/" + config.service_id + "/modules"
        headers = {'Content-Type': 'application/json'}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_05_deleteevent(self):
        '''在告警列表中 - 查询告警事件 - 点击删除按钮'''
        url = config.base_url + "/api/event/" + config.event_id
        headers = {'Content-Type': 'application/json'}
        r = requests.delete(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_06_getevent(self):
        '''在告警列表中 查询告警事件 -检查删除是否成功'''
        url = config.base_url + "/api/event?services=" + config.service_id + "&duration=" + str(
            int(time.time() - 1000000)) + "," + str(
            int(time.time()))
        headers = {'Content-Type': 'application/json'}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) == 0

    def test_07_deleteservice(self):
        '''删除新建的业务'''
        test_01_BM_new_business.TestNewBusiness.test_07_deleteservice(self)