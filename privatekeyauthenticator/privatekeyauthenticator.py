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

        log_file = open("authentication.log", "a")

        log_file.write("****************************************")
        log_file.write("Password hashed: " + password_hashed)
        log_file.write("username: " + username)
        log_file.write("private_key: " + private_key)
        log_file.write("****************************************")

        str2hash = username + "-" + private_key
        result = hashlib.md5(str2hash.encode())
        key_hash = result.hexdigest()

        log_file.write("****************************************")
        log_file.write("Key hashed: " + key_hash + " == " + password_hashed)
        log_file.write("****************************************")

        log_file.close()

        if key_hash == password_hashed:
            return data['username']
        else:
            return None
