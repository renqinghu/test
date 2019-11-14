import requests
import pytest
import config
import json
import time


class TestMultiEvent(object):
    """
    民生调用链---根源系统定位
    """
    node_key = "node.bztest001"
    modigynode_key = "node.bztest002"
    name = "rqh_test"

    def test_01_getapiservice(self) -> object:
        '''获取一跳信息 [get] /api/service/5da6d1759f62af470efb08be/graph?maxHop=1'''
        global service_id
        url = config.base_url + "/api/service/" + config.service_id + "/graph?maxHop=1"
        headers = {'Content-Type': 'application/json'}
        # data = {"details": {"events": [{"event_id": "5da6b5421a870b4165bb7bcc", "time": 1524689580}]}}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        service_id = jobs["data"]["instances"][0]["service_id"]

    def test_01_getapiservice2(self) -> object:
        '''获取二跳信息 [get] /api/service/5da6d1759f62af470efb08be/graph?maxHop=2'''
        url = config.base_url + "/api/service/" + config.service_id + "/graph?maxHop=2"
        headers = {'Content-Type': 'application/json'}
        # data = {"details": {"events": [{"event_id": "5da6b5421a870b4165bb7bcc", "time": 1524689580}]}}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_01_getapiservice3(self) -> object:
        '''获取三跳信息 [get] /api/service/5da6d1759f62af470efb08be/graph?maxHop=3'''
        url = config.base_url + "/api/service/" + config.service_id + "/graph?maxHop=3"
        headers = {'Content-Type': 'application/json'}
        # data = {"details": {"events": [{"event_id": "5da6b5421a870b4165bb7bcc", "time": 1524689580}]}}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_01_getapiservice4(self) -> object:
        '''获取四跳信息 [get] /api/service/5da6d1759f62af470efb08be/graph?maxHop=4'''
        global service_id
        url = config.base_url + "/api/service/" + config.service_id + "/graph?maxHop=4"
        headers = {'Content-Type': 'application/json'}
        # data = {"details": {"events": [{"event_id": "5da6b5421a870b4165bb7bcc", "time": 1524689580}]}}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_01_getapiservice5(self) -> object:
        '''获取五跳信息 [get] /api/service/5da6d1759f62af470efb08be/graph?maxHop=5'''
        global service_id
        url = config.base_url + "/api/service/" + config.service_id + "/graph?maxHop=5"
        headers = {'Content-Type': 'application/json'}
        # data = {"details": {"events": [{"event_id": "5da6b5421a870b4165bb7bcc", "time": 1524689580}]}}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_01_getapiservice0(self) -> object:
        '''获取0跳信息 [get] /api/service/5da6d1759f62af470efb08be/graph?maxHop=0'''
        global service_id
        url = config.base_url + "/api/service/" + config.service_id + "/graph?maxHop=0"
        headers = {'Content-Type': 'application/json'}
        # data = {"details": {"events": [{"event_id": "5da6b5421a870b4165bb7bcc", "time": 1524689580}]}}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_01_getapiservice1001(self) -> object:
        '''超出最大跳数1000 [get] /api/service/5da6d1759f62af470efb08be/graph?maxHop=0'''
        global service_id
        url = config.base_url + "/api/service/" + config.service_id + "/graph?maxHop=1001"
        headers = {'Content-Type': 'application/json'}
        # data = {"details": {"events": [{"event_id": "5da6b5421a870b4165bb7bcc", "time": 1524689580}]}}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 400
        # assert jobs["msg"] == "OK"

    def test_02_geteventservice_id(self) -> object:
        '''获取事件服务信息 [get] api/event?services=service_id_1&duration=1508661837,1571733837&sort_field=time&order=ASC'''
        url = config.base_url + "api/event?services=" + service_id + "&duration=" + str(
            int(time.time() - 1000000)) + "," + str(
            int(time.time())) + "&sort_field=time&order=ASC"
        headers = {'Content-Type': 'application/json'}
        # data = {"details": {"events": [{"event_id": "5da6b5421a870b4165bb7bcc", "time": 1524689580}]}}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        global event_id
        event_id = jobs["data"]["events"]["event_id"]

    def test_03_getevent_id(self) -> object:
        '''查询事件详情信息 [get] /api/event/5da6d1759f62af470efb08be'''
        url = config.base_url + "/api/event/" + event_id
        headers = {'Content-Type': 'application/json'}
        # data = {"details": {"events": [{"event_id": "5da6b5421a870b4165bb7bcc", "time": 1524689580}]}}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        assert jobs["data"]["event_id"] == event_id
