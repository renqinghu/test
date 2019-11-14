import requests
import pytest
import config
import json
import time


class TestMultiLevel(object):
    """
    机器--多层级
    """
    service_id = ""
    name = "rqhtest005"

    def test_01_postNodeData(self):
        '''【多层级】 获取 Class 名称列表 [post] /api/node/data/metric/class'''
        url = config.base_url + "/api/node/data/metric/class"
        headers = {'Content-Type': 'application/json'}
        # 数据源 / 机器指标
        data = {"nodes": [
            "node.BCBSAP03",
            "node.BCB"]
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        global classNames
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        config.classNames = jobs["data"]

    def test_02_postNodeData(self):
        '''【多层级】获取 Instance 名称列表 [post] /api/node/data/metric/class/instance'''
        url = config.base_url + "/api/node/data/metric/class/instance"
        headers = {'Content-Type': 'application/json'}
        # 数据源 / 机器指标
        data = {"nodes": [
            "node.BCBSAP03",
            "node.BCB"],
            "classNames": config.classNames
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        config.instances = jobs["data"]

    def test_03_postNodeDataClassInstance(self):
        '''【多层级】 获取 column 名称列表 [post] /api/node/data/metric/class/instance/column'''
        url = config.base_url + "/api/node/data/metric/class/instance/column"
        headers = {'Content-Type': 'application/json'}
        # 数据源 / 机器指标
        data = {"nodes": [
            "node.BCBSAP03",
            "node.BCB"], "classNames": ['MEM', 'CPU', 'NET', 'DISK'], "instances": config.instances
        }

        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_04_postNodeDataClassInstance(self):
        '''获取 Metric 数据 [post] /api/node/data/get'''
        url = config.base_url + "/api/node/data/get?time=1571042768000,1571042900000"
        headers = {'Content-Type': 'application/json'}
        # 数据源 / 机器指标
        data = {"nodes": [
            "node.BCBSAP03",
            "node.BCB"], "metrics": [
            "net2##instance2##mem",
            "net1##instance2##cpu"
        ]
        }

        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_05_postNodeDataClassInstance(self):
        '''(multi=true)获取 Metric 数据 [post] /api/node/data/get'''
        url = config.base_url + "/api/node/data/get?time=1571042768000,1571042900000&multi=true"
        headers = {'Content-Type': 'application/json'}
        # 数据源 / 机器指标
        data = {"nodes": [
            "node.BCBSAP03",
            "node.BCB"], "metrics": [
            "net2##instance2##mem",
            "net1##instance2##cpu"
        ]
        }

        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_06_postNodeDataClassInstance(self):
        '''(multi=false)获取 Metric 数据 [post] /api/node/data/get'''
        url = config.base_url + "/api/node/data/get?time=" + str(int(time.time() - 1000000)) + "," + str(
            int(time.time())) + "&multi=false"
        headers = {'Content-Type': 'application/json'}
        # 数据源 / 机器指标
        data = {"nodes": [
            "node.BCBSAP03",
            "node.BCB"], "metrics": [
            "net2##instance2##mem",
            "net1##instance2##cpu"
        ]
        }

        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_07_postNodeDataClassInstance(self):
        '''(multi=false)获取 Metric 数据 [post] /api/node/data/get'''
        url = config.base_url + "/api/node/data/get?time=1570982400,1571155200&multi=false"
        headers = {'Content-Type': 'application/json'}
        # 数据源 / 机器指标
        data = {
            "nodes": [
                "node.BCBSAP01",
                "node.BCBSAP02"
            ],
            "metrics": [
                "net2##instance2##mem",
                "net1##instance2##cpu"
            ]
        }

        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
