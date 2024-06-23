import http.client
import os
import unittest
from urllib.request import urlopen
import requests
import json
import pytest
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL_STAGING')
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    

    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")


    def test_api_hello(self):
        print('---------------------------------------')
        print('Starting - integration test API Hello')
        #List
        url = BASE_URL+""
        response = requests.get(url)
        print('Response Hello URL:' + str(response))
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a {url}"
        )
        print('End - integration test API Hello')


    def test_api_list_users(self):
        print('---------------------------------------')
        print('Starting - integration test List Users')
        #List
        url = BASE_URL+"/users"
        response = requests.get(url)
        print('Response Hello URL:' + str(response))
        json_response = response.json()
        
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a {url}"
        )
        self.assertEqual(
            json_response[0], json.loads('{"pass": "2595336547d795d0c236799d00fb590c32b47d3f76795cb733cf49aee64e7176","user": "pedro"}'), 
            "Error en la petición API a {url}"
        )
        self.assertEqual(
            json_response[1], json.loads('{"pass": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4","user": "pedro2"}'), 
            "Error en la petición API a {url}"
        )
        print('End - integration test List Users')