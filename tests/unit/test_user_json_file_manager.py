import os
import pytest
import unittest
import json
from dotenv import load_dotenv
from app.UsersJsonFileManager import UsersJsonFileManager

load_dotenv()
file_name = os.getenv('USERS_FILE')

@pytest.mark.unit
class TestUsersJsonFileManager(unittest.TestCase):
    def setUp(self):
        self.manager = UsersJsonFileManager(file_name)
        self.input_entry = json.loads('{"user":"abcd","pass":"1234"}')
        self.output_entry = json.loads('{"user": "abcd", "pass":"03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"}')
    
    def test_create_method_return_correct_result(self):
        test_input_entry2 = json.loads('{"user": "klwmn", "pass": "8765"}')
        test_output_entry2 = json.loads('{"user": "klwmn", "pass": "cccd34d95dc5294d17177274e6a7b25a569fda7d823f2aa59ba63dfba9f8e013"}')
        self.assertEqual(test_output_entry2, self.manager.create_entry(test_input_entry2))

    def test_get_method_return_correct_result(self):
        self.assertEqual(self.output_entry, self.manager.read_entry(int(0)))  

    def test_create_method_fail_already_exit_user(self):
        self.assertRaises(TypeError, self.manager.create_entry, self.input_entry)

    def test_create_method_fail_bad_format_input(self):
        test_input_entry2 = json.loads('{"useer": "klmn", "pass": "1234"}')
        test_input_entry3 = json.loads('{"user": "klmn", "pa-ss": "1234"}')
        self.assertRaises(TypeError, self.manager.create_entry, test_input_entry2)    
        self.assertRaises(TypeError, self.manager.create_entry, test_input_entry3) 



