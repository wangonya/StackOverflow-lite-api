""" We imported os and then set the basedir variable as a relative path from any place we call it to this file.
We then set up a base Config() class with some basic setup that our other config classes inherit from.
Now we’ll be able to import the appropriate config class based on the current environment.
Thus, we can use environment variables to choose which settings we’re going to use based on the environment
- e.g., local, staging, production. (https://realpython.com/flask-by-example-part-1-project-setup/) """

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'stack-overflow-lite-secret'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
