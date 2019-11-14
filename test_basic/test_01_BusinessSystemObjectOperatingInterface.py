import requests
import pytest
import config
import json
from test_basic import test_04_EventObjectOperatingInterface


# import test_04_EventObjectOperatingInterface

def setup_module():
    print("开始测试")


def teardown_module():
    print("结束测试")


class TestAPIService(object):
    """
    http://192.168.115.51:3000/project/29/interface/api/3863
    服务
    """
    service_id = ""
    name = "rqhtest005"

    def test_01_getapiservice(self):
        '''获取业务系统列表[get] /api/service'''
        url = config.base_url + "/api/service"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_01_getapiservicepage(self):
        '''获取业务系统列表[get] /api/service'''
        url = config.base_url + "/api/service?page=1&size=10&type=top&name=ATM&level=A"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_02_postapiservice(self):
        '''创建业务系统[post] /api/service'''
        url = config.base_url + "/api/service"
        headers = {'Content-Type': 'application/json'}
        data = {"name": self.name}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        config.service_id = jobs["data"]["service_id"]
        assert jobs["code"] == 201
        assert jobs["msg"] == "Created"
        assert len(jobs["data"]) != 0
        assert jobs["data"]["name"] == self.name

    def test_03_getservice_id(self):
        '''(验证创建业务是否成功)获获取业务系统信息[get] /api/service/:service_id'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        assert jobs["data"]["name"] == self.name

    def test_04_modifyservice_id(self):
        '''修改业务系统配置[post] /api/service/:service_id'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}
        # data = {"name":"test002","monitored_kpi":["kpi.test-661"],"modules":["5db29e771a870ba0355be777"],"alert_rules":[],"receiver":{"email_inherit":True,"email":["zjinn@bizseer.com"]},"ips":[],"success_codes":[],"quoridor_id":""}
        data = {"name": "test002", "monitored_kpi": ["kpi.test-661"], "modules": ["5da6af651a870b4165bb7b94"],
                "alert_rules": [], "receiver": {"email_inherit": True, "email": ["zjinn@bizseer.com"]}, "ips": [],
                "success_codes": [], "quoridor_id": "调用链标识", "level": ""}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        assert jobs["data"]["name"] == "test002"
        assert jobs["data"]["receiver"]["email"][0] == "zjinn@bizseer.com"

    def test_05_getservice_id(self):
        '''(验证修改是否成功)获获取业务系统信息[get] /api/service/:service_id'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        assert jobs["data"]["name"] == "test002"
        assert jobs["data"]["receiver"]["email"][0] == "zjinn@bizseer.com"

    def test_05_geteventid_graph(self):
        '''(民生调用链) [get] /api/event/{eventId}/graph'''
        test_04_EventObjectOperatingInterface.TestEventInterface.test_02_postapievent(self)
        url = config.base_url + "/api/event/" + config.event_id + "/graph"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        r = requests.get(url, headers=headers)
        test_04_EventObjectOperatingInterface.TestEventInterface.test_13_deleteapievent_id(self)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200

    def test_06_deleteservice_id(self):
        '''删除业务系统[delete] /api/service/:service_id'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}

        r = requests.delete(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_07_getservice_id(self):
        '''(验证删除是否成功)获获取业务系统信息[get] /api/service/:service_id'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 404

    def test_08_getservice_id(self):
        '''(验证删除是否成功)获获取业务系统信息[get] /api/service/:service_id'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 404
