from src.settings import app_config
from .memory_store import MemoryStore

def get_config_store(app_config):
    if app_config.ENV in {'dev', 'test'}:
        store = MemoryStore(app_config.CONF_DATA_SOURCE)
    else:
        raise ValueError("Enivornment '{}' not supported".format(app_config.ENV))
    return store

store = get_config_store(app_config)
