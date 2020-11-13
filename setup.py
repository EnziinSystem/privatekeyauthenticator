#!/usr/bin/env python

from setuptools import setup

setup(name='privatekeyauthenticator',
      version='1.0',
      description='Private Key Authenticator for Jupyterhub',
      author='Kevin Nguyen',
      license='MIT',
      author_email='enziinsystem@gmail.com',
      url='https://github.com/EnziinSystem/privatekeyauthenticator',
      packages=['privatekeyauthenticator'],
      install_requires=[
          'jupyterhub',
      ],
      )
