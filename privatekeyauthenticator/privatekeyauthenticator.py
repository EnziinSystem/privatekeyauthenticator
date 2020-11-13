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

        # file_log = open("/var/log/authentication.log", "a")
        # file_log.write("****************************************\n")
        # file_log.write("Password hashed: " + str(password_hashed) + "\n")
        # file_log.write("username: " + str(username) + "\n")
        # file_log.write("private_key: " + str(private_key) + "\n")
        # file_log.write("****************************************\n")

        str2hash = str(username) + "-" + str(private_key)
        result = hashlib.md5(str2hash.encode())
        key_hash = result.hexdigest()

        # file_log.write("****************************************\n")
        # file_log.write("Key hashed: " + str(key_hash) + " == " + str(password_hashed) + "\n")
        # file_log.write("****************************************\n")
        # file_log.close()

        if key_hash == str(password_hashed):
            return data['username']
        else:
            return None
