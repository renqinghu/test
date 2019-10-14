import requests
import pytest
import config
import json
import time
import math


class TestModularInterface(object):
    """
    Test get a list of jobs from jenkins
    """
    node_key = "node.bztest001"
    modigynode_key = "node.bztest002"
    name = "rqhtest007"

    def test_01_getmodule(self):
        '''获获取模块列表[get] /api/module'''
        url = config.base_url + "/api/module"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        config.module_id = jobs["data"][0]["module_id"]

    def test_02_getmodule_id(self):
        '''获取指定模块[get] /api/module/:module_id'''
        url = config.base_url + "/api/module/" + config.module_id
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_03_postapimodule(self):
        '''创建模块[post] /api/module'''
        url = config.base_url + "/api/module"
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": self.name,
            "nodes": ["node.MOBSDB01", "node.MOBSDB02"]
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs,data)
        assert jobs["code"] == 201
        assert jobs["msg"] == "Created"
        config.module_id = jobs["data"]["module_id"]

    def test_03_getmodule_id(self):
        '''(验证创建模块是否成功)获取指定模块[get] /api/module/:module_id'''
        url = config.base_url + "/api/module/" + config.module_id
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert r.text.count(self.name) >= 1

    def test_04_modifymodule_id(self):
        '''修改模块内容[post] /api/module/:module_id'''
        url = config.base_url + "/api/module/" + config.module_id
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "rqhtestDB02",
            "nodes": ["node.MOBSDB01", "node.MOBSDB02"]
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs,data)
        assert jobs["code"] == 200
        assert jobs["data"]["name"] == "rqhtestDB02"

    def test_04_getmodule_id(self):
        '''(验证修改模块内容是否成功)获取指定模块[get] /api/module/:module_id'''
        url = config.base_url + "/api/module/" + config.module_id
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert r.text.count("rqhtestDB02") >= 1

    def test_05_deletemodule_id(self):
        '''删除模块[delete] /api/module/:module_id'''
        url = config.base_url + "/api/module/" + config.module_id
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": self.name,
            "nodes": ["node.MOBSDB01", "node.MOBSDB02"]
        }
        r = requests.delete(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs,data)
        assert jobs["code"] == 200
        # assert json["msg"] == "Created"
        # config.module_id = json["data"]["module_id"]

    def test_06_getmodule_id(self):
        '''(验证删除模块是否成功)获取指定模块[get] /api/module/:module_id'''
        url = config.base_url + "/api/module/" + config.module_id
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 404
