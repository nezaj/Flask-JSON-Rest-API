import json

from flask import url_for
import pytest

@pytest.mark.usefixtures('client', 'store')
class TestUnitsCreate(object):

    @classmethod
    def setup_class(cls):
        cls.unit_id = "test.com"
        cls.unit_conf = {"unit_id": cls.unit_id, "unit_type": "button"}

    def _delete_unit(self):
        return self.store.delete_unit(self.unit_id)

    def _response(self):
        url = url_for('units.create')
        data = json.dumps(self.unit_conf)
        return self.client.post(url, data=data, content_type="application/json")

    def test_create_returns_200(self):
        res = self._response()
        assert res.status_code == 200
        self._delete_unit()

    def test_create_returns_json(self):
        res = self._response()
        assert res.mimetype == 'application/json'
        self._delete_unit()

    def test_create_adds_new_config_to_store(self):
        assert self.unit_id not in self.store.get_all_units()
        self._response()
        assert self.unit_id in self.store.get_all_units()
        self._delete_unit()

    def test_create_returns_400_if_content_type_is_not_json(self):
        unit_id = "moop.com"
        url = url_for('units.create')
        data = json.dumps({"unit_id": unit_id, "unit_type": "button"})
        res = self.client.post(url, data=data, content_type="text/html")
        assert res.status_code == 400
        assert res.mimetype == 'application/json'
