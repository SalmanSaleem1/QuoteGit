import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '1234657889'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///quotes.db'


class TestConfig(BaseConfig):
    DEBUG = True
    Testing = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///quotes.db'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
