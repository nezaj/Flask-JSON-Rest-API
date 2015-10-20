"""
API routes for interacting with button configurations
"""
from flask import abort, Blueprint, jsonify, request

from src.data import store

blueprint = Blueprint('units', __name__)

@blueprint.route('/units', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    # TODO: Add validation
    data = store.create_unit(request.json)
    return jsonify(data)

@blueprint.route('/units/<unit_id>', methods=['DELETE'])
def delete(unit_id):
    data = store.delete_unit(unit_id)
    if data is None:
        abort(400)
    return jsonify(data)

@blueprint.route('/units', methods=['GET'])
def index():
    data = store.get_all_units()
    return jsonify(data)

@blueprint.route('/units/<unit_id>', methods=['GET'])
def show(unit_id):
    data = store.get_unit(unit_id)
    if data is None:
        abort(404)
    return jsonify(data)

@blueprint.route('/units/<unit_id>', methods=['PUT'])
def update(unit_id):
    if not request.json:
        abort(400)
    data = store.update_unit(unit_id, request.json)
    if data is None:
        abort(404)
    return jsonify(data)
