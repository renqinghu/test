import requests
import pytest
import config
import json
import time


class TestNewBusiness(object):
    """
    业务监控--【新建业务 -> 查询 -> 删除 -> 查询】
    """
    node_key = "node.bztest001"
    modigynode_key = "node.bztest002"
    name = "rqh_test"

    def test_01_postservice(self):
        '''新建业务[post] /api/service'''
        url = config.base_url + "/api/service"
        headers = {'Content-Type': 'application/json'}
        data = {"name": self.name}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 201
        assert jobs["msg"] == "Created"
        assert len(jobs["data"]) != 0
        assert jobs["data"]["name"] == self.name
        config.service_id = jobs["data"]["service_id"]
        print(config.service_id)

    def test_02_getservice_id(self):
        '''查询新建业务[get] /api/service/:service_id'''
        print(config.service_id)
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}
        # data = {"name":self.name}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        assert jobs["data"]["name"] == self.name
        jobs["data"]["service_id"] == config.service_id

    def test_03_getmodule(self):
        '''查询module[get] /api/service/5da58b8f9f62af470efa0456/modules'''
        url = config.base_url + "/api/service/" + config.service_id + "/modules"
        headers = {'Content-Type': 'application/json'}
        # data = {"name":self.name}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_04_getkpi(self):
        '''查询kpi[get] /api/kpi/extremelySimplified?query=&limit=100'''
        url = config.base_url + "/api/kpi/extremelySimplified?query=&limit=100"
        headers = {'Content-Type': 'application/json'}
        # data = {"name":self.name}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_05_getkpi(self):
        '''查询module page [get] /api/module/page?page=1&size=100'''
        url = config.base_url + "/api/module/page?page=1&size=100"
        headers = {'Content-Type': 'application/json'}
        # data = {"name":self.name}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_06_postkpinames(self):
        '''查询kpi name [post] /api/kpi/names'''
        url = config.base_url + "/api/kpi/names"
        headers = {'Content-Type': 'application/json'}
        data = {"kpi_keys": []}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_07_deleteservice(self) -> object:
        '''删除新建业务 [delete] /api/service/5da591489f62af470efa045e'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}
        # data = {"kpi_keys":[]}
        r = requests.delete(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_08_getmodulepage(self):
        '''查询module page[get] /api/module/page?page=1&size=10'''
        url = config.base_url + "/api/module/page?page=1&size=10"
        headers = {'Content-Type': 'application/json'}
        # data = {"kpi_keys":[]}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_09_getevent(self):
        '''查询event [get] /api/event?services=5bc9bd155210e6104d6bafad&duration=1571048005,1571134405'''
        url = config.base_url + "/api/event?services=" + config.service_id + "&duration=1571048005,1571134405"
        headers = {'Content-Type': 'application/json'}
        # data = {"kpi_keys":[]}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
