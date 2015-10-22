from flask import Flask, jsonify

from . import service, units

def create_app(config_obj):
    """ Factory for creating app """
    app = Flask(__name__)
    app.config.from_object(config_obj)
    app.register_blueprint(service.views.blueprint)
    app.register_blueprint(units.views.blueprint)
    register_errorhandlers(app)
    return app

def register_errorhandlers(app):
    def handler(error):
        response = jsonify(message=str(error))
        response.status_code = getattr(error, 'code', 500)
        return response

    for errcode in [400, 404, 500]:
        app.errorhandler(errcode)(handler)
