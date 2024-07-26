import pytest
import unittest
import hashlib
import os
from dotenv import load_dotenv
from app.tools.security_toolbox import security_toolbox


load_dotenv()
secret_key = os.getenv('SECRECT_JWT')


@pytest.mark.unit
class TestUsersJsonFileManager(unittest.TestCase):
    def setUp(self):
        self.my_security_tools = security_toolbox(secret_key)
        pass
    
    def test_get_sha256_signature_correct_result(self):
        num_data = 98547
        string_data = '12345'
        list_data = [1,2,3,4,5]

        hash_object = hashlib.sha256()
        hash_object.update(str(num_data).encode('utf-8'))
        signature_num_calculated = hash_object.hexdigest()  

        hash_object = hashlib.sha256()
        hash_object.update(string_data.encode('utf-8'))
        signature_str_calculated = hash_object.hexdigest()

        hash_object = hashlib.sha256()
        hash_object.update(str(list_data).encode('utf-8'))
        signature_list_calculated = hash_object.hexdigest()
        
        self.assertEqual(signature_num_calculated, self.my_security_tools.get_sha256_signature(num_data))
        self.assertEqual(signature_str_calculated, self.my_security_tools.get_sha256_signature(string_data))
        self.assertEqual(signature_list_calculated, self.my_security_tools.get_sha256_signature(list_data))


    def test_get_sha256_signature_fail(self): 
        num_data = 98547
        string_data = '12345'
        list_data = [1,2,3,4,5] 

        signature_num_calculated = 3333
        signature_str_calculated = 'adgggre'
        signature_list_calculated = 23432

        self.assertNotEqual(signature_num_calculated, self.my_security_tools.get_sha256_signature(num_data))
        self.assertNotEqual(signature_str_calculated, self.my_security_tools.get_sha256_signature(string_data))
        self.assertNotEqual(signature_list_calculated, self.my_security_tools.get_sha256_signature(list_data))


    def test_get_sha256_signature_correct_result(self):
        user = 'pepe01'
        expiration_time_min = 2

        token = self.my_security_tools.get_jwt_token(user, expiration_time_min)
        credentials_from_token = self.my_security_tools.decode_jwt_token(token)
        user_decoded_from_toke = credentials_from_token['user_id']
        self.assertEqual(user, str(user_decoded_from_toke))