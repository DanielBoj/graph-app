# Graphic generation API for Tarjeta Ciudadano stats
## Dependencies
[Dependencies File](dependencies.txt)

## Usage
Test &rarr; 
- Install dependencies with `pip install -r dependencies.txt`
- From /app run 'gunicorn main:app'

### Endpoints
- Base &rarr; '/estadisticas-tarjeta-ciudadana/api/v1/graficos'
- City Card Enrollment Graphics &rarr; '/enrollment'
    - Params: JSON with 'totalCitizens' and 'totalEnrollment' keys
- City Bus Usage Graphics &rarr; '/bus'
    - Params: JSON with 'totalRides' and 'inYearRides' keys

api_blueprint = Blueprint('api', __name__, url_prefix='/estadisticas-tarjeta-ciudadana/api/v1/graficos')
api_blueprint.route('/enrollment', methods=['POST'])(city_key_enrollment_pie_chart)
api_blueprint.route('/bus/total-year', methods=['POST'])(bus_year_rides_pie_chart)
api_blueprint.route('/bus/total-year-registered', methods=['POST'])(bus_year_registered_rides_pie_chart)
api_blueprint.route('/bus/total-year-card-type', methods=['POST'])(bus_year_fisical_and_virtual_card_rides_pie_chart)
api_blueprint.route('/bus/annual', methods=['POST'])(annual_bus_rides_bar_chart)
api_blueprint.route('/bus/monthly', methods=['POST'])(monthly_bus_rides_bar_chart)
api_blueprint.route('/bus/daily', methods=['POST'])(daily_bus_rides_bar_chart)

app_version_api_blueprint = Blueprint('app_version_api', __name__, url_prefix='/estadisticas-tarjeta-ciudadana/api/v1/app-version')
app_version_api_blueprint.route('', methods=['GET'])(app_version_handler)