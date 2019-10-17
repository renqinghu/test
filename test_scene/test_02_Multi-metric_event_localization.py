import requests
import pytest
import config
import json
import time


class TestMultiEvent(object):
    """
    多指标事件根因定位
    """
    node_key = "node.bztest001"
    modigynode_key = "node.bztest002"
    name = "rqh_test"

    def test_01_postnodedata(self):
        '''模块-获取node data [post] /api/node/data/get?&time=1524685980,1524696780&multi=false'''
        url = config.base_url + "/api/node/data/get?&time=1524685980,1524696780&multi=false"
        headers = {'Content-Type': 'application/json'}
        data = {"nodes": ["node.BCBSAP06", "node.BCBSAP04", "node.BCBSAP01", "node.BCBSAP05", "node.BCBSAP03",
                          "node.BCBSAP09", "node.BCBSAP02", "node.BCBSAP08", "node.BCBSAP10", "node.BCBSAP07"],
                "metrics": ["MEM##InstanceBCBSAP06##MEM", "MEM##InstanceBCBSAP04##MEM", "MEM##InstanceBCBSAP01##MEM",
                            "MEM##InstanceBCBSAP05##MEM", "MEM##InstanceBCBSAP03##MEM", "MEM##InstanceBCBSAP09##MEM",
                            "MEM##InstanceBCBSAP02##MEM", "MEM##InstanceBCBSAP08##MEM", "MEM##InstanceBCBSAP10##MEM",
                            "MEM##InstanceBCBSAP07##MEM"]}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_02_postnodedata(self):
        '''类型-获取node data [post] /api/node/data/get?&time=1524685980,1524696780&multi=false'''
        url = config.base_url + "/api/node/data/get?&time=1524685980,1524696780&multi=false"
        headers = {'Content-Type': 'application/json'}
        data = dict(nodes=["node.BCBSAP10", "node.BCBSAP09", "node.BCBSAP07"],
                    metrics=["NET##InstanceBCBSAP10##NETWRITE", "NET##InstanceBCBSAP09##NETWRITE",
                             "NET##InstanceBCBSAP07##NETWRITE"])
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_03_postnodedata(self):
        '''机器-获取node data [post] /api/node/data/get?&time=1524685980,1524696780&multi=false'''
        url = config.base_url + "/api/node/data/get?&time=1524685980,1524696780&multi=false"
        headers = {'Content-Type': 'application/json'}
        data = dict(nodes=["node.BCBSAP09"], metrics=["NET##InstanceBCBSAP09##NETWRITE"])
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_04_postnodedata(self):
        '''实例-获取node data [post] /api/node/data/get?&time=1524685980,1524696780&multi=false'''
        url = config.base_url + "/api/node/data/get?&time=1524685980,1524696780&multi=false"
        headers = {'Content-Type': 'application/json'}
        data = {"nodes": ["node.BCBSAP06"], "metrics": ["MEM##InstanceBCBSAP06##MEM"]}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_05_postnodedata(self):
        '''重新分析 [put] /api/task/fluxrank'''
        url = config.base_url + "/api/task/fluxrank"
        headers = {'Content-Type': 'application/json'}
        data = {"details": {"events": [{"event_id": "5da6b5421a870b4165bb7bcc", "time": 1524689580}]}}
        r = requests.put(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 202
        assert jobs["msg"] == "Accepted"
        assert len(jobs["data"]) != 0
