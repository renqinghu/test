import requests
import pytest
import config
import json


class TestAPIService(object):
    """
    Test get a list of jobs from jenkins
    """
    service_id = ""
    name = "rqhtest005"

    def test_01_getapiservice(self):
        '''获取业务系统列表[get] api/service'''
        url = config.base_url + "/api/service"
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200

    def test_02_postapiservice(self):
        '''创建业务系统[post] api/service'''
        url = config.base_url + "/api/service"
        headers = {'Content-Type': 'application/json'}
        data = {"name": self.name}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        config.service_id = jobs["data"]["service_id"]
        assert jobs["code"] == 201

    def test_03_getservice_id(self):
        '''(验证创建业务是否成功)获获取业务系统信息[get] /api/service/:service_id'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["data"]["name"] == self.name

    def test_04_modifyservice_id(self):
        '''修改业务系统配置[post] /api/service/:service_id'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test002",
            "monitored_kpi": ["kpi.mobilebanks.trans_volume", "kpi.mobilebanks.resp_time"],
            "modules": ["5b078c2f4c7d9c44c44f79f8"],
            "alert_rules": [
                {
                    "type": "frequency",
                    "duration": 300,
                    "kpi_min_thr": 2,
                    "frequency": 10
                }
            ],
            "receiver": {
                "email": ["zjinn@bizseer.com"]
            }
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 200
        assert jobs["data"]["name"] == "test002"

    def test_04_getservice_id(self):
        '''(验证修改是否成功)获获取业务系统信息[get] /api/service/:service_id'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["data"]["name"] == "test002"

    def test_05_deleteservice_id(self):
        '''删除业务系统[delete] /api/service/:service_id'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}

        r = requests.delete(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200

    def test_05_getservice_id(self):
        '''(验证删除是否成功)获获取业务系统信息[get] /api/service/:service_id'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}

        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 400
