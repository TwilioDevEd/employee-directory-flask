import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    SECRET_KEY = 'secret-key'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' +
                               os.path.join(basedir, 'default.sqlite'))
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
    TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', None)


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' +
                               os.path.join(basedir, 'dev.sqlite'))


class TestConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' +
                               os.path.join(basedir, 'test.sqlite'))
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True

config_env_files = {
    'test': 'employee_directory_flask.config.TestConfig',
    'development': 'employee_directory_flask.config.DevelopmentConfig',
}
