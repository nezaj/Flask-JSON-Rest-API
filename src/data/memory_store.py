"""
Store implementation using in-memory data
"""
import json
import os

from .store_interface import StoreInterface

class MemoryStore(object):
    __implements__ = (StoreInterface, )

    def __init__(self, conf_dir):
        self.conf_dir = conf_dir
        self.data = self._load_conf_files(conf_dir)

    def _load_conf_files(self, conf_dir):
        confs = {}
        for conf in os.listdir(conf_dir):
            conf = os.path.join(conf_dir, conf)
            if conf.endswith(".json"):
                conf_json = self._load_conf_file(conf)
                unit_id, unit_config = self._process_conf_file(conf_json)
                confs[unit_id] = unit_config
        return confs

    @staticmethod
    def _load_conf_file(conf):
        """ Loads a json config file """
        with open(conf) as conf_file:
            conf_data = json.load(conf_file)
        return conf_data["data"]

    @staticmethod
    def _process_conf_file(conf_json):
        """
        Returns json configuration data in a format we can easily parse and work
        with
        """
        unit_id = conf_json["unit_id"]
        return unit_id, conf_json

    def create_unit(self, params):
        unit_id, unit_conf = self._process_conf_file(params)
        self.data[unit_id] = unit_conf
        return unit_conf

    def delete_unit(self, unit_id):
        if unit_id in self.data:
            unit_conf = self.data[unit_id]
            del self.data[unit_id]
            return unit_conf

    def get_all_units(self):
        return self.data

    def get_unit(self, unit_id):
        return self.data.get(unit_id)

    def update_unit(self, unit_id, params):
        if unit_id in self.data:
            self.data[unit_id].update(params)
            return self.data[unit_id]
