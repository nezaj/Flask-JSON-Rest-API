import pytest

from src.data import store as _store

@pytest.fixture(scope='function')
def store(request):
    request.instance.store = _store
    return _store
