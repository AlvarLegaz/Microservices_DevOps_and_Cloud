from app import util
from app.UserAccountManager import UserAccountManager

user_manager = UserAccountManager()

username = 'pedro7'
password_ok = '1234'
password_wrong='4178'

# user_manager.signup(username, password)
print("Test Signin OK:")
print(user_manager.signin(username, password_ok))

token = util.get_jwt_token(username, 30)
util.decode_jwt_token(token)

print("Test Signin Fail:")
print(user_manager.signin(username, password_wrong))


