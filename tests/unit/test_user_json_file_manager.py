import os
import json
import pytest
import unittest
from dotenv import load_dotenv
from app.UsersJsonFileManager import UsersJsonFileManager

load_dotenv()
file_name = os.getenv('USERS_FILE')

@pytest.mark.unit
class TestUsersJsonFileManager(unittest.TestCase):
    def setUp(self):
        self.manager = UsersJsonFileManager(file_name)
    
    def test_create_method_returns_correct_result(self):
        test_entry = {
        "user": "abcd",
        "pass": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
        }
        self.assertEqual(test_entry, self.manager.create_entry({'user':'abcd','pass':'1234'}))
        self.assertRaises(TypeError, self.manager.create_entry({'user':'abcd','pass':'1234'}))
