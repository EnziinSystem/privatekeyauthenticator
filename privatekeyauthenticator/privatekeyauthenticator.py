from jupyterhub.auth import Authenticator
from tornado import gen
import hashlib
import os


class PrivateKeyAuthenticator(Authenticator):
    @gen.coroutine
    def authenticate(self, handler, data):
        password_hashed = data['password']
        username = data['username']
        private_key = os.getenv('DATA_SCIENCE_ACCESS_KEY')

        print("****************************************")
        print("Password hashed: " + password_hashed)
        print("username: " + username)
        print("private_key: " + private_key)
        print("****************************************")

        str2hash = username + "-" + private_key
        result = hashlib.md5(str2hash.encode())
        key_hash = result.hexdigest()

        print("****************************************")
        print("Key hashed: " + key_hash + " == " + password_hashed)
        print("****************************************")

        if key_hash == password_hashed:
            return data['username']
        else:
            return None
