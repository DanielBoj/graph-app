from flask import Blueprint
from .handlers import *

api_blueprint = Blueprint('api', __name__, url_prefix='/estadisticas-tarjeta-ciudadana/api/v1/graficos')

api_blueprint.route('/enrollment', methods=['POST'])(city_key_enrollment_pie_chart)
api_blueprint.route('/bus/total-year', methods=['POST'])(bus_year_rides_pie_chart)
api_blueprint.route('/bus/total-year-registered', methods=['POST'])(bus_year_registered_rides_pie_chart)
api_blueprint.route('/bus/total-year-card-type', methods=['POST'])(bus_year_fisical_and_virtual_card_rides_pie_chart)
api_blueprint.route('/bus/annual', methods=['POST'])(annual_bus_rides_bar_chart)
api_blueprint.route('/bus/monthly', methods=['POST'])(monthly_bus_rides_bar_chart)
api_blueprint.route('/bus/daily', methods=['POST'])(daily_bus_rides_bar_chart)


api_blueprint.route('/test', methods=['GET'])(test)
