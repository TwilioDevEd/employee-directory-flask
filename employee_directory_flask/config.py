import os

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URI')
        or f"sqlite:///{os.path.join(basedir, 'dev.sqlite')}"
    )


class TestConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SERVER_NAME = 'server.test'


config_env_files = {
    'testing': 'employee_directory_flask.config.TestConfig',
    'development': 'employee_directory_flask.config.DevelopmentConfig',
    'production': 'employee_directory_flask.config.DefaultConfig',
}
