from flask import Blueprint
from .handlers import city_key_enrollment_pie_chart, bus_rides_pie_chart , test

api_blueprint = Blueprint('api', __name__, url_prefix='/estadisticas-tarjeta-ciudadana/api/v1/graficos')

api_blueprint.route('/enrollment', methods=['POST'])(city_key_enrollment_pie_chart)
api_blueprint.route('/bus', methods=['POST'])(bus_rides_pie_chart)
api_blueprint.route('/test', methods=['GET'])(test)
