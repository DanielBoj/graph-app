from flask import Blueprint
from .handlers import *

# api_blueprint = Blueprint('api', __name__, url_prefix='/estadisticas-tarjeta-ciudadana/api/v1/graficos')

# api_blueprint.route('/enrollment', methods=['POST'])(city_key_enrollment_graphs)

# api_blueprint.route('/purchases', methods=['POST'])(recharges_and_bonus_uses_graphs)

# api_blueprint.route('/courses', methods=['POST'])(courses_and_workshops_graphs)

# api_blueprint.route('/bus/total-year', methods=['POST'])(bus_year_rides_pie_chart)
# api_blueprint.route('/bus/annual', methods=['POST'])(annual_bus_rides_bar_chart)
# api_blueprint.route('/bus/monthly', methods=['POST'])(monthly_bus_rides_bar_chart)
# api_blueprint.route('/bus/daily-by-month', methods=['POST'])(daily_by_month_bus_rides_bar_chart)
# api_blueprint.route('/bus/weekly', methods=['POST'])(weekly_bus_rides_bar_chart)
# api_blueprint.route('/bus/daily', methods=['POST'])(daily_bus_rides_bar_chart)

# Nuevo enrutado

api_blueprint = Blueprint('api', __name__, url_prefix='/estadisticas-tarjeta-ciudadana/api/v1/graficos')

# Enrutado para gráficos de inscripciones (enrollment)
api_blueprint.route('/enrollment', methods=['POST'])(city_key_enrollment_graphs)
api_blueprint.route('/enrollment/in-year-monthly', methods=['POST'])(in_year_monthly_enrollments)
api_blueprint.route('/enrollment/in-month-daily', methods=['POST'])(in_month_daily_enrollments)
api_blueprint.route('/enrollment/weekly', methods=['POST'])(weekly_enrollments)
api_blueprint.route('/enrollment/daily', methods=['POST'])(daily_enrollments)

# Enrutado para gráficos de recargas y usos de bonos (purchases)
api_blueprint.route('/purchases', methods=['POST'])(recharges_and_bonus_uses_graphs)
api_blueprint.route('/purchases/daily-by-month', methods=['POST'])(daily_by_month_recharges_and_bonus_uses)
api_blueprint.route('/purchases/weekly', methods=['POST'])(weekly_recharges_and_bonus_uses)
api_blueprint.route('/purchases/daily', methods=['POST'])(daily_recharges_and_bonus_uses)

# Enrutado para gráficos de cursos y talleres (courses)
api_blueprint.route('/courses', methods=['POST'])(courses_and_workshops_graphs)
api_blueprint.route('/courses/yearly', methods=['POST'])(yearly_courses_bar_chart)
api_blueprint.route('/courses/monthly', methods=['POST'])(monthly_courses_bar_chart)
api_blueprint.route('/courses/weekly', methods=['POST'])(weekly_courses_bar_chart)
api_blueprint.route('/courses/daily', methods=['POST'])(daily_courses_bar_chart)

# Enrutado para gráficos de viajes en autobús (bus)
api_blueprint.route('/bus/total-year', methods=['POST'])(bus_year_rides_pie_chart)
api_blueprint.route('/bus/annual', methods=['POST'])(annual_bus_rides_bar_chart)
api_blueprint.route('/bus/monthly', methods=['POST'])(monthly_bus_rides_bar_chart)
api_blueprint.route('/bus/daily-by-month', methods=['POST'])(daily_by_month_bus_rides_bar_chart)
api_blueprint.route('/bus/weekly', methods=['POST'])(weekly_bus_rides_bar_chart)
api_blueprint.route('/bus/daily', methods=['POST'])(daily_bus_rides_bar_chart)