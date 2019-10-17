import requests
import pytest
import config
import json
import time

from test_scene import test_04_Multidimensional_anomaly_location



def test_test():
    a = test_04_Multidimensional_anomaly_location.TestMultiEvent()
    a.test_01_postnodedata()
