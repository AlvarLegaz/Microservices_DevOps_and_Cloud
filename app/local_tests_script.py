import os
from dotenv import load_dotenv
from app.security_toolbox import security_toolbox

load_dotenv()
secret_key = os.getenv('SECRECT_JWT')

username = 'pedro7'
password_ok = '1234'
password_wrong='4178'

# user_manager.signup(username, password)
#print("Test Signin OK:")
#print(user_manager.signin(username, password_ok))

my_security_tools = security_toolbox(secret_key)

token = my_security_tools.get_jwt_token(username, 30)
print(f"Token generated with expiration time: {token}")

credentials_decoded = my_security_tools.decode_jwt_token(token)
print(f"Credential decoded from token: {credentials_decoded}")




