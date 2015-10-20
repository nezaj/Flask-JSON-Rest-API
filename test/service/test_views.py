from flask import url_for
import pytest

@pytest.mark.usefixtures('client')
class TestServiceViews(object):

    def test_health_returns_200(self):
        url = url_for("service.health")
        res = self.client.get(url)
        assert res.status_code == 200

    def test_bad_route_returns_json_mimetype(self):
        url = url_for("service.bad_route")
        res = self.client.get(url)
        assert res.mimetype == 'application/json'

    def test_internal_error_returns_json_mimetype(self):
        url = url_for("service.internal_error")
        res = self.client.get(url)
        assert res.mimetype == 'application/json'

    def test_bad_request_returns_json_mimetype(self):
        url = url_for("service.bad_request")
        res = self.client.get(url)
        assert res.mimetype == 'application/json'
