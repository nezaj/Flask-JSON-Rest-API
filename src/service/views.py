"""
Service-oriented routes like health
"""
from flask import abort, Blueprint

blueprint = Blueprint('service', __name__)

@blueprint.route('/health', methods=['GET'])
def health():
    """ Used to test if webserver is running """
    return "All is well"

@blueprint.route('/400', methods=['GET'])
def bad_request():
    """ Used to test 500 pages, specifically that it returns json """
    abort(400)

@blueprint.route('/404', methods=['GET'])
def bad_route():
    """ Used to test 404 pages, specifically that it returns json """
    abort(404)

@blueprint.route('/500', methods=['GET'])
def internal_error():
    """ Used to test 500 pages, specifically that it returns json """
    abort(500)
