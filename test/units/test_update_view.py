import json

from flask import url_for
import pytest

@pytest.mark.usefixtures('client', 'store')
class TestUnitsUpdate(object):

    @classmethod
    def setup_class(cls):
        cls.unit_id = "test.com"
        cls.unit_conf = {"unit_id": cls.unit_id, "unit_type": "button"}
        cls.unit_conf_update = {"unit_id": cls.unit_id, "unit_type": "immersive"}

    def _create_unit(self):
        return self.store.create_unit(self.unit_conf)

    def _delete_unit(self):
        return self.store.delete_unit(self.unit_id)

    def _response(self):
        url = url_for('units.update', unit_id=self.unit_id)
        data = json.dumps(self.unit_conf_update)
        return self.client.put(url, data=data, content_type="application/json")

    def test_update_returns_200(self):
        self._create_unit()
        res = self._response()
        assert res.status_code == 200
        self._delete_unit()

    def test_update_returns_json(self):
        self._create_unit()
        res = self._response()
        assert res.mimetype == 'application/json'
        self._delete_unit()

    def test_update_returns_updated_config(self):
        self._create_unit()
        res = self._response()
        res_json = json.loads(res.data)
        assert res_json == self.unit_conf_update
        self._delete_unit()

    def test_update_returns_400_if_content_type_is_not_json(self):
        unit_id = "moop.com"
        url = url_for('units.update', unit_id=unit_id)
        data = json.dumps({"unit_id": unit_id, "unit_type": "button"})
        res = self.client.put(url, data=data, content_type="text/html")
        assert res.status_code == 400
        assert res.mimetype == 'application/json'

    def test_update_returns_404_if_config_not_found(self):
        unit_id = "moop.com"
        url = url_for('units.update', unit_id=unit_id)
        data = json.dumps({"unit_id": unit_id, "unit_type": "button"})
        res = self.client.put(url, data=data, content_type="application/json")
        assert res.status_code == 404
        assert res.mimetype == 'application/json'
