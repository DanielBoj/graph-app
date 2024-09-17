# Graphic generation API for Tarjeta Ciudadano stats
## Dependencies
[Dependencies File](dependencies.txt)

## Usage
Test &rarr; Run 'python3 main.py'

### Endpoints
- Base &arr; '/estadisticas-tarjeta-ciudadana/api/v1/graficos'
- City Card Enrollment Graphics &arr; '/enrollment'
-- Params: JSON with 'totalCitizens' and 'totalEnrollment' keys
- City Bus Usage Graphics &arr; '/bus'
-- Params: JSON with 'totalRides' and 'inYearRides' keys
- Test &arr; '/test' Shows a test graphic