import jwt
import datetime
import hashlib


class security_toolbox:

    def __init__(self, secret_key):
        self.secret_key = secret_key


    def get_sha256_signature(self, data):
        hash_object = hashlib.sha256()
        hash_object.update(str(data).encode('utf-8'))
        return hash_object.hexdigest()


    def get_jwt_token(self, user, time_life_minutes):
        payload = {
        'user_id': user,
        'exp': datetime.datetime.now() + datetime.timedelta(minutes=time_life_minutes) 
        }
        encoded_token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return encoded_token


    def decode_jwt_token(self, token):
        try:
            decoded_payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return decoded_payload
        
        except jwt.ExpiredSignatureError:
            print("El token ha expirado.")
        except jwt.DecodeError:
            print("Error al decodificar el token.")    