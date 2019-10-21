import requests
import pytest
import config
import json
import time


class TestMultiEvent(object):
    """
    多维度异常定位 volcano
    """
    node_key = "node.bztest001"
    modigynode_key = "node.bztest002"
    name = "rqh_test"

    def test_01_postnodedata(self) -> object:
        '''模块-获取node data [put] /api/task/volcano'''
        url = config.base_url + "/api/task/volcano"
        headers = {'Content-Type': 'application/json'}
        data = {"details": {"events": [{"event_id": "5da6b5421a870b4165bb7bcc", "time": 1524689580}]}}
        r = requests.put(url, data=json.dumps(data), headers=headers)
        jobs = r.json()
        config.pprint(url, jobs, data)
        assert jobs["code"] == 202
        assert jobs["msg"] == "Accepted"
        assert len(jobs["data"]) != 0
