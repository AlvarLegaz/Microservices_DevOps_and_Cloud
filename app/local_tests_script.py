from app import security_toolbox
from app.UserAccountManager import UserAccountManager

user_manager = UserAccountManager()

username = 'pedro7'
password_ok = '1234'
password_wrong='4178'

# user_manager.signup(username, password)
print("Test Signin OK:")
print(user_manager.signin(username, password_ok))

token = security_toolbox.get_jwt_token(username, 30)
print(f"Token generated with expiration time: {token}")

credentials_decoded = security_toolbox.decode_jwt_token(token)
print(f"Credential decoded from token: {credentials_decoded}")



