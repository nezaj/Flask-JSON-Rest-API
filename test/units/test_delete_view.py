import json

from flask import url_for
import pytest

@pytest.mark.usefixtures('client', 'store')
class TestUnitsDelete(object):

    @classmethod
    def setup_class(cls):
        cls.unit_id = "test.com"

    def _create_unit(self):
        unit_conf = {"unit_id": self.unit_id}
        return self.store.create_unit(unit_conf)

    def _response(self):
        url = url_for('units.delete', unit_id=self.unit_id)
        return self.client.delete(url)

    def test_delete_returns_200(self):
        self._create_unit()
        res = self._response()
        assert res.status_code == 200

    def test_delete_returns_json(self):
        self._create_unit()
        res = self._response()
        assert res.mimetype == 'application/json'

    def test_delete_returns_deleted_config(self):
        to_delete = self._create_unit()
        res = self._response()
        res_json = json.loads(res.data)
        assert res_json == to_delete

    def test_delete_returns_400_if_config_not_found(self):
        url = url_for('units.delete', unit_id='moop')
        res = self.client.delete(url)
        assert res.status_code == 400
        assert res.mimetype == 'application/json'
