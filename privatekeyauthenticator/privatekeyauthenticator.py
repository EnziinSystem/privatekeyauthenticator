from jupyterhub.auth import Authenticator
from tornado import gen
import hashlib
import os
import logging

logging.basicConfig(level=logging.DEBUG, file='/opt/jupyterhub/authentication.log')


class PrivateKeyAuthenticator(Authenticator):
    @gen.coroutine
    def authenticate(self, handler, data):
        password_hashed = data['password']
        username = data['username']
        private_key = os.getenv('DATA_SCIENCE_ACCESS_KEY')

        logging.debug("****************************************")
        logging.debug("Password hashed: " + password_hashed)
        logging.debug("username: " + username)
        logging.debug("private_key: " + private_key)
        logging.debug("****************************************")

        str2hash = username + "-" + private_key
        result = hashlib.md5(str2hash.encode())
        key_hash = result.hexdigest()

        logging.debug("****************************************")
        logging.debug("Key hashed: " + key_hash + " == " + password_hashed)
        logging.debug("****************************************")

        if key_hash == password_hashed:
            return data['username']
        else:
            return None
