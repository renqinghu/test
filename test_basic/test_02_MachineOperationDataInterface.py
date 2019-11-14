import requests
import pytest
import config
import json
import time


class TestMachineNode(object):
    """
    http://192.168.115.51:3000/project/29/interface/api/3742
    机器
    """
    node_key = "node.bztest001"
    modigynode_key = "node.bztest002"
    name = "rqhtest005"

    def test_01_getapinode(self):
        '''获取机器节点列表[get] /api/node'''
        url = config.base_url + "/api/node"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_02_putapinode(self):
        '''创建机器节点[put] /api/node/:node_key'''
        url = config.base_url + "/api/node/" + self.node_key
        headers = {'Content-Type': 'application/json'}

        r = requests.put(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 201
        assert jobs["msg"] == "Created"
        assert len(jobs["data"]) != 0
        assert jobs["data"]["node_key"] == self.node_key
        assert jobs["data"]["name"] == self.node_key

    def test_02_getapinode(self):
        '''(验证创建机器节点是否成功)获取机器节点列表[get] /api/node'''
        url = config.base_url + "/api/node"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        assert r.text.count("node.bztest001") >= 1

    def test_03_modifyapinode(self):
        '''机器节点重命名[post] /api/node/:node_key/name'''
        url = config.base_url + "/api/node/" + self.node_key + "/name"
        headers = {'Content-Type': 'application/json'}
        data = {"name": self.modigynode_key}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        assert jobs["data"]["node_key"] == self.node_key
        assert jobs["data"]["name"] == self.modigynode_key

    def test_03_getapinode(self):
        '''(验证重命名机器节点是否成功)获取机器节点列表[get] /api/node'''
        url = config.base_url + "/api/node"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        assert r.text.count(self.modigynode_key) >= 1
        assert r.text.count(self.node_key) >= 1

    def test_04_getapinodedata(self):
        '''获取机器节点多维数据[get] /api/node/:node_key/data'''
        url = config.base_url + "/api/node/" + self.node_key + "/data?time=" + str(int(time.time()))
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_05_postapinodedata(self):
        '''提交机器节点多维数据[post] /api/node/:node_key/data'''
        url = config.base_url + "/api/node/" + self.node_key + "/data?time=" + str(int(time.time()))
        headers = {'Content-Type': 'application/json'}
        data = {
            "header": ["time", "CPU_Usage", "Mem_Usage", "Idle_Process"],
            "values": [
                [int(time.time()), 34, 10000000, 12],
                [int(time.time()), 40, 11000000, 10],
                [int(time.time()), 40, 11000000, 10],
                [int(time.time()), 40, 11000000, 10],
                [int(time.time()), 40, 11000000, 10],
                [int(time.time()), 40, 11000000, 10],
                [int(time.time()), 40, 11000000, 10],
                [int(time.time()), 40, 11000000, 10],
                [int(time.time()), 40, 11000000, 10]
            ],
            "auto_create": True
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_06_getapinodedata(self):
        '''获取机器节点多维数据表头[get] /api/node/:node_key/data/metric'''
        url = config.base_url + "/api/node/" + self.node_key + "/data/metric"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    # def test_07_getapinodedata(self):
    #     '''批量获取机器节点多维数据[get] /api/node/data'''
    #     url = config.base_url + "/api/node/data"
    #     headers = {'Content-Type': 'application/json'}
    #     data = {"nodes": [self.node_key], "time": str(int(time.time()))}
    #     r = requests.post(url, data=json.dumps(data),headers=headers)
    #     jobs = r.json()
    #     config.pprint(url, jobs)
    #     assert jobs["code"] == 200

    def test_08_postapinodedata(self):
        '''批批量提交机器节点多维数据[post] /api/node/data'''
        url = config.base_url + "/api/node/data"
        headers = {'Content-Type': 'application/json'}
        data = {
            "auto_create": True,
            "data": [
                {
                    "node_key": self.node_key,
                    "header": ["time", "CPU_Usage", "Mem_Usage", "Idle_Process"],
                    "values": [
                        [int(time.time()), 34, 10000000, 12],
                        [int(time.time()), 40, 11000000, 10],
                        [int(time.time()), 40, 11000000, 10],
                        [int(time.time()), 40, 11000000, 10],
                        [int(time.time()), 40, 11000000, 10],
                        [int(time.time()), 40, 11000000, 10],
                        [int(time.time()), 40, 11000000, 10],
                        [int(time.time()), 40, 11000000, 10],
                        [int(time.time()), 40, 11000000, 10]
                    ]
                },
            ]
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_09_getapinodedata(self):
        '''批量获取机器节点多维数据表头[get] /api/node/data/metric'''
        url = config.base_url + "/api/node/data/metric"
        headers = {'Content-Type': 'application/json'}
        data = {"nodes": [self.node_key]}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_10_deleteapinode(self):
        '''删除机器节点[delete] /api/node/:node_key'''
        url = config.base_url + "/api/node/" + self.node_key
        headers = {'Content-Type': 'application/json'}

        r = requests.delete(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_11_getapinode(self):
        '''(验证删除机器节点是否成功)获取机器节点列表[get] /api/node'''
        url = config.base_url + "/api/node"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        assert r.text.count(self.node_key) == 0
        assert r.text.count(self.modigynode_key) == 0

    def test_12_getapinodepage(self):
        '''(获取机器指标列表)获取机器节点列表[get] /api/node/page'''
        url = config.base_url + "/api/node/page"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_13_getapinodepage(self):
        '''(获取机器指标列表)获取机器节点列表[get] /api/node/page'''
        url = config.base_url + "/api/node/page?query=node&page=1&size=1"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0