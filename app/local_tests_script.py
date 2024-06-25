from app.UserAccountManager import UserAccountManager

user_manager = UserAccountManager()

username = 'pedro7'
password_ok = '1234'
password_wrong='4178'

# user_manager.signup(username, password)
user_manager.signin(username,password_ok)
user_manager.signin(username,password_wrong)
