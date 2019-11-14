import requests
import pytest
import config
import json
import time


class TestAPIService(object):
    """
    民生告警规则测试用例
    """
    service_id = ""
    name = "rqhtest005"
    kpi = "kpi.BS-junit__trans_count_total1"
    kpi2 = "kpi.BS-junit__trans_count_total2"

    def test_01_createkpi(self):
        '''创建kpi [put] /api/kpi/kpi.BS-junit__trans_count_total'''
        url = config.base_url + "/api/kpi/" + self.kpi2
        headers = {'Content-Type': 'application/json'}
        data = {
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
        assert jobs["code"] == 201
        assert jobs["msg"] == "Created"
        assert len(jobs["data"]) != 0