import os

class Config(object):
    # controls whether web interfance users are in Flask debug mode
    # (e.g. Werkzeug stack trace console, unminified assets)
    DEBUG = False

    # TODO: Set this to something proper later
    SECRET_KEY = "secret"

    # Useful directories
    SRC_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(SRC_DIR, 'data')
    TEST_DIR = os.path.join(os.path.dirname(SRC_DIR), 'test')

    # JSON file with unit configurations for in-memory stores
    CONF_DATA_SOURCE = os.path.join(DATA_DIR, 'confs')

class DevelopmentConfig(Config):
    ENV = 'dev'
    DEBUG = True

class TestConfig(Config):
    ENV = 'test'


config_dict = {
    'dev': DevelopmentConfig,
    'test': TestConfig,

    'default': DevelopmentConfig
}

app_config = config_dict[os.getenv('APP_ENV') or 'default']
