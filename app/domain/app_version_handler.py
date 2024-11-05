from flask import Response, Blueprint
import json

from configuration.config_loader import config


def app_version_handler():
    """
    Este método devuelve la versión de la aplicación cliente Android.
    ---
    responses:
        200:
            description: Versión de la aplicación cliente Android.
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            version:
                                type: string
                                description: Versión de la aplicación cliente Android.
                            date:
                                type: string
                                description: Fecha de la versión de la aplicación cliente Android.
    """

    app_version = {
        'version': config['app_version']['version'],
        'date': config['app_version']['date']
    }
    json_app_version = json.dumps(app_version)

    return Response(json_app_version, mimetype='application/json')


app_version_api_blueprint = Blueprint('app_version_api', __name__, url_prefix='/estadisticas-tarjeta-ciudadana/api/v1/app-version')
app_version_api_blueprint.route('', methods=['GET'])(app_version_handler)
