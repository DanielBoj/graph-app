from flask import Response, Blueprint

from configuration.config_loader import config


def app_version_handler():
    # Construct object with version and date
    app_version = {
        'version': config['app_version']['version'],
        'date': config['app_version']['date']
    }

    return Response(app_version, mimetype='application/json')


app_version_api_blueprint = Blueprint('app_version_api', __name__, url_prefix='/estadisticas-tarjeta-ciudadana/api/v1/app-version')
app_version_api_blueprint.route('', methods=['GET'])(app_version_handler)
