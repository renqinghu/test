import requests
import pytest
import config
import json
import time
from test_scene import test_01_BM_new_business


class TestNewBusiness(object):
    """
    业务监控--【添加kpi -> 配置 -> 获取服务模块 -> 查询kpi -> 点击发布配置按钮】
    """
    node_key = "node.bztest001"
    modigynode_key = "node.bztest002"
    name = "rqh_test"
    eventdesc = "测试新建告警事件"

    def test_01_postservice(self):
        '''创建kpi'''
        url = config.base_url + "/api/kpi/kpi.test-661"
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "zyx-交易量",
            "state": {
                "retrain": False,
                "concept_drift_time": 0,
                "activate": True,
                "in_concept_drift": False,
                "interval": 60
            },
            "user": "aiops"
        }
        r = requests.put(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)

    def test_02_getServiceModule(self):
        '''查询服务模块'''
        test_01_BM_new_business.TestNewBusiness().test_01_postservice()

        url = config.base_url + "/api/service/" + config.service_id + "/modules"
        headers = {'Content-Type': 'application/json'}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"

    def test_03_getkpi(self):
        '''查询kpi 【get】/api/kpi/extremelySimplified?query=&limit=100'''
        url = config.base_url + "/api/kpi/extremelySimplified?query=&limit=100"
        headers = {'Content-Type': 'application/json'}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        assert jobs["data"]["kpis"][0]["name"] == "zyx-交易量"
        assert jobs["data"]["kpis"][0]["kpi_key"] == "kpi.test-661"

    def test_04_getModulePage(self):
        '''查询module 【get】/api/module/page?page=1&size=100'''
        url = config.base_url + "/api/module/page?page=1&size=100"
        headers = {'Content-Type': 'application/json'}
        r = requests.get(url, headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0

    def test_05_postServiceConfig(self):
        '''点击发布配置按钮【post】/api/service/5da9268f1a870b1d64762452'''
        url = config.base_url + "/api/service/" + config.service_id
        headers = {'Content-Type': 'application/json'}
        data = {"name": test_01_BM_new_business.TestNewBusiness.name, "monitored_kpi": ["kpi.test-661"], "modules": ["5da6af651a870b4165bb7b94"],
                "alert_rules": [{"duration": 600, "type": "frequency", "kpi_min_thr": 1, "frequency": 5}],
                "receiver": {"email": ["test@qq.com"]}}
        r = requests.post(url, data=json.dumps(data),headers=headers)
        jobs = r.json()
        config.pprint(url, jobs)
        assert jobs["code"] == 200
        assert jobs["msg"] == "OK"
        assert len(jobs["data"]) != 0
        assert jobs["data"]["service_id"] == config.service_id
        assert jobs["data"]["name"] == test_01_BM_new_business.TestNewBusiness.name
        assert jobs["data"]["monitored_kpi"] == ["kpi.test-661"]
        assert jobs["data"]["alert_rules"][0]["duration"] == 600
        assert jobs["data"]["alert_rules"][0]["type"] == "frequency"
        assert jobs["data"]["alert_rules"][0]["kpi_min_thr"] == 1
        assert jobs["data"]["alert_rules"][0]["frequency"] == 5
        assert jobs["data"]["receiver"]["email"] == ["test@qq.com"]
