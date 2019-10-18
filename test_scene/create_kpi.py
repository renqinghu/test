import requests
import pytest
import config
import json
import time


class TestCreateKPI(object):
    """
    创建kpi
    """
    node_key = "node.bztest001"
    modigynode_key = "node.bztest002"
    name = "rqh_test"

    def test_01_postservice(self):
        '''新建业务[post] /api/service'''
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