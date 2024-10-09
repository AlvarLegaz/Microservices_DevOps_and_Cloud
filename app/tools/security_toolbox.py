import jwt
import datetime
import hashlib


class SecurityToolbox:

    def __init__(self, secret_key):
        self.secret_key = secret_key

    def get_sha256_signature(self, data):
        print(f"Original data: {data}")  # Debug prints
        hash_object = hashlib.sha256()
        hash_object.update(str(data).encode('utf-8'))
        signature = hash_object.hexdigest()
        print(f"Generated SHA-256 hash: {signature}")  # Debug print
        return signature

    def get_jwt_token(self, user, time_life_minutes):
        try:
            user_str = str(user)
            payload = {
                'user_id': user_str,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=time_life_minutes)
            }
            encoded_token = jwt.encode(payload, self.secret_key, algorithm='HS256')
            return encoded_token
        except Exception as e:
            raise Exception("SecurityToolbox exception - Fail encoding JWT token: " + str(e))

    def decode_jwt_token(self, token):
        try:
            decoded_payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return decoded_payload
        except jwt.ExpiredSignatureError:
            raise Exception("El token ha expirado.")
        except jwt.DecodeError:
            raise Exception("Error al decodificar el token.")      

if __name__ == '__main__':          # pragma: no cover
    # Uso de la clase
    my_toolbox = SecurityToolbox("sdasdasdas")

    print(my_toolbox.get_jwt_token('alvar',10))
