from src.app import create_app
from src.settings import DevelopmentConfig, TestConfig

def test_dev_config():
    app = create_app(DevelopmentConfig)
    assert app.config['ENV'] == 'dev'
    assert app.config['DEBUG'] is True

def test_test_config():
    app = create_app(TestConfig)
    assert app.config['ENV'] == 'test'
