"""
Configures pytest and fixtures for tests in this package
"""
import pytest

from src.app import create_app
from src.settings import TestConfig

def pytest_addoption(parser):
    """ Allows us to add --runslow as an argument to py.test so we can run tests marked slow """
    parser.addoption("--runslow", action="store_true", help="run slow tests")

def pytest_runtest_setup(item):
    """ Skip tests marked 'slow' unless we explicility asked to run them """
    if 'slow' in item.keywords and not item.config.getoption("--runslow"):
        pytest.skip("need --runslow option to run")

@pytest.fixture(scope='function')
def app(request):
    """
    Flask app instance fixture with an active request context.
    See: http://flask.pocoo.org/docs/0.10/reqcontext/
    """
    _app = create_app(TestConfig)
    request.instance.app = _app

    ctx = _app.test_request_context()
    ctx.push()

    request.addfinalizer(ctx.pop)
    return _app

@pytest.fixture(scope='function')
def client(app, request):
    request.instance.client = app.test_client()
