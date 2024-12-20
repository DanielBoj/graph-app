from flask import Blueprint
from .handlers import *

api_blueprint = Blueprint('api', __name__, url_prefix='/estadisticas-tarjeta-ciudadana/api/v1/graficos')

api_blueprint.route('/enrollment', methods=['POST'])(city_key_enrollment_graphs)

api_blueprint.route('/purchases', methods=['POST'])(recharges_and_bonus_uses_graphs)

api_blueprint.route('/courses', methods=['POST'])(courses_and_workshops_graphs)

api_blueprint.route('/bus/total-year', methods=['POST'])(bus_year_rides_pie_chart)
api_blueprint.route('/bus/annual', methods=['POST'])(annual_bus_rides_bar_chart)
api_blueprint.route('/bus/monthly', methods=['POST'])(monthly_bus_rides_bar_chart)
api_blueprint.route('/bus/daily-by-month', methods=['POST'])(daily_by_month_bus_rides_bar_chart)
api_blueprint.route('/bus/weekly', methods=['POST'])(weekly_bus_rides_bar_chart)
api_blueprint.route('/bus/daily', methods=['POST'])(daily_bus_rides_bar_chart)
