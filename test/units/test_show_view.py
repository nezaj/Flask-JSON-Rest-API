import json

from flask import url_for
import pytest

@pytest.mark.usefixtures('client', 'store')
class TestUnitsShow(object):

    def _get_unit_id(self):
        return self.store.get_all_units().keys()[0]

    def _response(self):
        unit_id = self._get_unit_id()
        url = url_for('units.show', unit_id=unit_id)
        return self.client.get(url)

    def test_show_returns_200(self):
        res = self._response()
        assert res.status_code == 200

    def test_show_returns_json(self):
        res = self._response()
        assert res.mimetype == 'application/json'

    def test_show_returns_one_config(self):
        res = self._response()
        res_json = json.loads(res.data)
        unit_id = self._get_unit_id()
        assert res_json == self.store.get_unit(unit_id)

    def test_show_returns_404_if_unit_id_does_not_exist(self):
        url = url_for('units.show', unit_id='moop')
        res = self.client.get(url)
        assert res.status_code == 404
        assert res.mimetype == 'application/json'
