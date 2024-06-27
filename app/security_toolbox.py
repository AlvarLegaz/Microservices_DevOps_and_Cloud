import jwt
import datetime
import hashlib

secret_key = 'mi_clave_secreta'

def get_sha256_signature(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode('utf-8'))
    return hash_object.hexdigest()

def get_jwt_token(user, time_life_minutes):
    payload = {
    'user_id': user,
    'exp': datetime.datetime.now() + datetime.timedelta(minutes=time_life_minutes) 
    }
    encoded_token = jwt.encode(payload, secret_key, algorithm='HS256')
    return encoded_token

def decode_jwt_token(token):
    try:
        decoded_payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return decoded_payload
    
    except jwt.ExpiredSignatureError:
        print("El token ha expirado.")
    except jwt.DecodeError:
        print("Error al decodificar el token.")    