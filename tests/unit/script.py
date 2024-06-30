import jwt
import datetime
import hashlib
import os
from dotenv import load_dotenv


num_data = 98547
string_data = '12345'

hash_object = hashlib.sha256()
hash_object.update(str(string_data).encode('utf-8'))
signature_num_calculated = hash_object.hexdigest()  

hash_object = hashlib.sha256()
hash_object.update(string_data.encode('utf-8'))
signature_str_calculated = hash_object.hexdigest()