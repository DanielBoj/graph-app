# API de generación de gráficos de estadísticas de la Tarjeta Ciudadana
## Dependencias
aniso8601==9.0.1
attrs==24.2.0
blinker==1.8.2
click==8.1.7
dnspython==2.7.0
flasgger==0.9.7.1
Flask==3.0.3
gunicorn==23.0.0
itsdangerous==2.2.0
Jinja2==3.1.4
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
kaleido==0.2.1
Markdown==3.7
MarkupSafe==3.0.2
mistune==3.0.2
numpy==2.1.3
packaging==24.1
pandas==2.2.3
plotly==5.24.1
python-dateutil==2.9.0.post0
pytz==2024.2
PyYAML==6.0.2
referencing==0.35.1
rpds-py==0.20.1
six==1.16.0
tenacity==9.0.0
tzdata==2024.2
Werkzeug==3.1.2

## Ruta Swagger
`/apidocs/`

## Uso
### Desarrollo
- Navegar al directorio de la aplicación mediante `$ cd ./app` 
- Generar un entorno virtual con `$ pipenv shell`
- Instalar las dependencias con `$ pipenv install -r ./requirements.txt`
- Desde le directorio /app ejecutar `$ gunicorn main:app`

## Endpoints
### 1. Versión de la aplicación cliente
- URL &rarr; `/estadisticas-tarjeta-ciudadana/api/v1/app-version/app-version`
- Método &rarr; `GET`
- Parámetros &rarr; Ninguno
- Retorno &rarr; JSON con clave:
``
<br>
- Base URL &rarr; `/estadisticas-tarjeta-ciudadana/api/v1/graficos`

### 2. Gráficos de inscripción de la Tarjeta Ciudadana
- URL &rarr; `/enrollment`
- Método &rarr; `POST`
- Parámetros &rarr; JSON con claves:
`{
  "dailyEnrollment": [],
  "monthlyEnrollment": [],
  "totalYearNotRegisteredEnrollments": 0,
  "totalYearRegisteredEnrollments": 0,
  "weeklyEnrollment": [],
  "yearlyEnrollment": []
}`
- Retorno &rarr; Webview con los siguientes gráficos:
    1. Gráfico de pastel con la cantidad de ciudadanos empadronados y no empadronados
    2. Gráfico de barras con la cantidad de registros en cada mes del año
    3. Gráfico de barras con la cantidad de registros en cada día del mes
    4. Gráfico de barras con la cantidad de registros en cada dia de la semana
    5. Gráfico de barras con la cantidad de registros en cada hora del día

### 3. Gráficos de recargas y usos de los bonos
- URL &rarr; `/purchases`
- Método &rarr; `POST`
- Parámetros &rarr; JSON con claves:
`{
  "dailyByMonthPurchases": [],
  "dailyPurchases": [],
  "monthlyPurchases": [],
  "weeklyPurchases": []
}`
- Retorno &rarr; Webview con los siguientes gráficos:
    1. Gráfico de barras con la cantidad de recargas en cada mes del año
    2. Gráfico de barras con la cantidad de recargas en cada día del mes
    3. Gráfico de barras con la cantidad de recargas en cada dia de la semana
    4. Gráfico de barras con la cantidad de recargas en cada hora del día

### 4. Gráficos de cursos y talleres
- URL &rarr; `/courses`
- Método &rarr; `POST`
- Parámetros &rarr; JSON con claves:
`{
  "dailyFreeCourses": [],
  "dailyPayedCourses": [],
  "monthlyByDayFreeCourses": [],
  "monthlyByDayPayedCourses": [],
  "totalEndedCourses": 0,
  "totalOnCurseCourses": 0,
  "totalYearFreeCourses": 0,
  "totalYearPayedCourses": 0,
  "weeklyFreeCourses": [],
  "weeklyPayedCourses": [],
  "yearlyByMonthFreeCourses": [],
  "yearlyByMonthPayedCourses": []
}`
- Retorno &rarr; Webview con los siguientes gráficos:
    1. Gráfico de quesito con la cantidad de cursos finalizados y en curso
    2. Grafico de quesito con la cantidad de cursos gratuitos y de pago
    3. Gráfico de multibarras con la cantidad de inscripciones en cada mes del año para cursos gratuitos y de pago
    4. Gráfico de multibarras con la cantidad de inscripciones en cada día del mes para cursos gratuitos y de pago
    5. Gráfico de multibarras con la cantidad de inscripciones en cada dia de la semana para cursos gratuitos y de pago
    6. Gráfico de multibarras con la cantidad de inscripciones en cada hora del día para cursos gratuitos y de pago

### 5. Gráficos de uso anual del transporte público
- URL &rarr; `/bus/total-year`
- Método &rarr; `POST`
- Parámetros &rarr; JSON con claves:
`{
  "inYearRides": 0,
  "totalFisicalCardRides": 0,
  "totalNotRegistered": 0,
  "totalRegistered": 0,
  "totalRides": 0,
  "totalVirtualCardRides": 0
}`
- Retorno &rarr; Webview con los siguientes gráficos:
    1. Gráfico de quesito con la cantidad de viajes realizados en el año y la cantidad de total de viajes desde el inicio del sistema
    2. Gráfico de quesito con la cantidad de viajes de ciudadanos empadronados y no empadronados
    3. Gráfico de quesito con la cantidad de viajes de ciudadanos con tarjeta física y virtual

### 6. Gráficos de barras de uso anual del transporte público
- URL &rarr; `/bus/annual`
- Método &rarr; `POST`
- Parámetros &rarr; JSON con claves:
`{
  "rides": []
}`
- Retorno &rarr; Webview con un gráfico de barras con la cantidad de viajes realizados en cada año desde el inicio del sistema

### 7. Gráficos de barras de uso mensual del transporte público
- URL &rarr; `/bus/monthly`
- Método &rarr; `POST`
- Parámetros &rarr; JSON con claves:
``
- Retorno &rarr; Webview con un gráfico de barras con la cantidad de viajes realizados en cada mes del año

### 8. Gráfico de barrar de uso diario a lo largo de un mes del transporte público
- URL &rarr; `/bus/daily-by-month`
- Método &rarr; `POST`
- Parámetros &rarr; JSON con claves:
`{
  "rides": []
}`
- Retorno &rarr; Webview con un gráfico de barras con la cantidad de viajes realizados en cada día del mes

### 9. Gráficos de barras de uso semanal del transporte público
- URL &rarr; `/bus/weekly`
- Método &rarr; `POST`
- Parámetros &rarr; JSON con claves:
`{
  "rides": []
}`
- Retorno &rarr; Webview con un gráfico de barras con la cantidad de viajes realizados en cada día de la semana

### 10. Gráficos de barras de uso diario del transporte público
- URL &rarr; `/bus/daily`
- Método &rarr; `POST`
- Parámetros &rarr; JSON con claves:
`{
  "rides": []
}`
- Retorno &rarr; Webview con un gráfico de barras con la cantidad de viajes realizados en cada hora del día