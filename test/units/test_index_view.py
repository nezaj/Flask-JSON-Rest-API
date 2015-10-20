import json

from flask import url_for
import pytest

@pytest.mark.usefixtures('client', 'store')
class TestUnitsIndex(object):

    def _response(self):
        url = url_for('units.index')
        return self.client.get(url)

    def test_index_returns_200(self):
        res = self._response()
        assert res.status_code == 200

    def test_index_returns_json(self):
        res = self._response()
        assert res.mimetype == 'application/json'

    def test_index_returns_all_configs(self):
        res = self._response()
        res_json = json.loads(res.data)
        assert res_json == self.store.get_all_units()
