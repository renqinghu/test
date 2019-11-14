# import requests
# import pytest
# import config
# import json
# import time
#
#
# class TestAPIService(object):
#     """
#     民生告警规则测试用例
#     """
#     service_id = ""
#     name = "rqhtest005"
#     kpi = "kpi.BS-junit__trans_count_total1"
#     kpi2 = "kpi.BS-junit__trans_count_total2"
#
#     @pytest.mark.skip("ss")
#     def test_01_createkpi(self):
#         '''创建kpi [put] /api/kpi/kpi.BS-junit__trans_count_total'''
#         url = config.base_url + "/api/kpi/" + self.kpi
#         headers = {'Content-Type': 'application/json'}
#         data = {
#             "state": {
#                 "retrain": False,
#                 "concept_drift_time": 0,
#                 "activate": True,
#                 "in_concept_drift": False,
#                 "interval": 60
#             },
#             "user": "aiops"
#         }
#         r = requests.put(url, data=json.dumps(data), headers=headers)
#         jobs = r.json()
#         config.pprint(url, jobs)
#         assert jobs["code"] == 201
#         assert jobs["msg"] == "OK"
#         assert len(jobs["data"]) != 0
#
#     @pytest.mark.skip("ss")
#     def test_02_createservice(self):
#         '''创建service [post] /api/service'''
#         url = config.base_url + "/api/service"
#         headers = {'Content-Type': 'application/json'}
#         data = {
#             "name": "junit17-微信银行"
#         }
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#         jobs = r.json()
#         config.pprint(url, jobs)
#         assert jobs["code"] == 201
#         assert jobs["msg"] == "Created"
#         assert len(jobs["data"]) != 0
#         global service_id
#         service_id = jobs["data"]["service_id"]
#
#     @pytest.mark.skip("ss")
#     def test_03_updateservice(self):
#         '''更新service [post] /api/service'''
#         url = config.base_url + "/api/service/" + service_id
#         headers = {'Content-Type': 'application/json'}
#         data = {
#             "name": "junit17-微信银行",
#             "monitored_kpi": [
#                 "kpi.BS-junit23__trans_count_total",
#                 "kpi.BS-junit23__succ_count_total",
#                 "kpi.BS-junit23__fail_count_total",
#                 "kpi.BS-junit23__resp_count_total",
#                 "kpi.BS-junit23__unresp_count_total",
#                 "kpi.BS-junit23__duration_avg",
#                 "kpi.BS-junit23__resp_p",
#                 "kpi.BS-junit23__succ_p"
#             ],
#             "alert_rules": [
#                 [
#                     {
#                         "duration": 120,
#                         "type": "anomaly_frequency",
#                         "kpis": [
#                             "kpi.BS-junit23__trans_count_total",
#                             "kpi.BS-junit23__succ_count_total",
#                             "kpi.BS-junit23__fail_count_total",
#                             "kpi.BS-junit23__resp_count_total",
#                             "kpi.BS-junit23__unresp_count_total",
#                             "kpi.BS-junit23__duration_avg",
#                             "kpi.BS-junit23__resp_p",
#                             "kpi.BS-junit23__succ_p"
#                         ],
#                         "kpi_min_thr": 1,
#                         "frequency": 1
#                     },
#                     {
#                         "op": "gt",
#                         "kpi": "kpi.BS-junit23__trans_count_total",
#                         "type": "single_value",
#                         "value": 30
#                     },
#                     {
#                         "type": "alert_level",
#                         "strategy": "system"
#                     }
#                 ]
#             ]
#         }
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#         jobs = r.json()
#         config.pprint(url, jobs)
#         assert jobs["code"] == 200
#         assert jobs["msg"] == "OK"
#         assert len(jobs["data"]) != 0
#
#     @pytest.mark.skip("ss")
#     def test_04_pushdata(self):
#         '''创建service [post] /api/kpi/kpi.BS-junit0__trans_count_total/data'''
#         url = config.base_url + "/api/kpi/" + self.kpi + "/data"
#         headers = {'Content-Type': 'application/json'}
#         data = {
#             "header": [
#                 "time",
#                 "anomaly",
#                 "value",
#                 "level",
#                 "lower",
#                 "upper"
#             ],
#             "values": [
#                 [
#                     int(time.time()),
#                     True,
#                     10,
#                     5,
#                     1.1,
#                     10.1
#                 ]
#             ]
#         }
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#         jobs = r.json()
#         config.pprint(url, jobs)
#         assert jobs["code"] == 200
#         assert jobs["msg"] == "OK"
#
#     @pytest.mark.skip("ss")
#     def test_05_pushdata(self):
#         '''创建service [post] /api/kpi/kpi.BS-junit0__trans_count_total/data'''
#         url = config.base_url + "/api/kpi/" + self.kpi + "/data"
#         headers = {'Content-Type': 'application/json'}
#         data = {
#             "header": [
#                 "time",
#                 "anomaly",
#                 "value",
#                 "level",
#                 "lower",
#                 "upper"
#             ],
#             "values": [
#                 [
#                     int(time.time()),
#                     True,
#                     12,
#                     5,
#                     1.1,
#                     10.1
#                 ]
#             ]
#         }
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#         jobs = r.json()
#         config.pprint(url, jobs)
#         assert jobs["code"] == 200
#         assert jobs["msg"] == "OK"
#
#     def test_06_pushdata(self):
#         '''创建service [post] /api/kpi/kpi.BS-junit0__trans_count_total/data'''
#         url = config.base_url + "/api/kpi/" + self.kpi + "/data"
#         headers = {'Content-Type': 'application/json'}
#         data = {
#             "header": [
#                 "time",
#                 "anomaly",
#                 "value",
#                 "level",
#                 "lower",
#                 "upper"
#             ],
#             "values": [
#                 [
#                     int(time.time()),
#                     True,
#                     12,
#                     5,
#                     1.1,
#                     10.1
#                 ]
#             ]
#         }
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#         jobs = r.json()
#         config.pprint(url, jobs)
#         assert jobs["code"] == 200
#         assert jobs["msg"] == "OK"
#
#     def test_07_pushdata(self):
#         '''创建service [post] /api/kpi/kpi.BS-junit0__trans_count_total/data'''
#         url = config.base_url + "/api/kpi/" + self.kpi2 + "/data"
#         headers = {'Content-Type': 'application/json'}
#         data = {
#             "header": [
#                 "time",
#                 "anomaly",
#                 "value",
#                 "level",
#                 "lower",
#                 "upper"
#             ],
#             "values": [
#                 [
#                     int(time.time()),
#                     True,
#                     12,
#                     5,
#                     1.1,
#                     10.1
#                 ]
#             ]
#         }
#         r = requests.post(url, data=json.dumps(data), headers=headers)
#         jobs = r.json()
#         config.pprint(url, jobs)
#         assert jobs["code"] == 200
#         assert jobs["msg"] == "OK"
