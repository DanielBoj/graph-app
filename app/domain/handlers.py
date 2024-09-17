from plotly import graph_objs as go
from flask import Response, request, render_template

from configuration.config_loader import config

import plotly.io as pio
pio.kaleido.scope.default_format = 'svg'
pio.kaleido.scope.default_scale = 1


def city_key_enrollment_pie_chart():

    payload = request.get_json()
    total_enrollment = int(payload['totalEnrollment'])
    total_citizens = int(payload['totalCitizens'])
    not_enrolled = total_citizens - total_enrollment

    labels = [config['label']['enrolled'], config['label']['not_enrolled']]
    values = [total_enrollment, not_enrolled]

    layout = go.Layout(title=config['title']['city_key_enrollment_pie_chart_title'].format(total_enrollment, total_citizens))

    pie_graph = go.Pie(labels=labels, values=values)
    fig = go.Figure(data=[pie_graph], layout=layout)
    
    img_bytes = fig.to_image(format='svg', engine='kaleido')
    return Response(img_bytes, mimetype='media/svg')

def bus_rides_pie_chart():

    payload = request.get_json()
    total_rides = int(payload['totalRides'])
    in_year_rides = int(payload['inYearRides'])

    labels = [config['label']['total_bus_rides'], config['label']['in_year_bus_rides']]
    values = [total_rides, in_year_rides]

    layout = go.Layout(title=config['title']['bus_rides_pie_chart_title']).format(total_rides, in_year_rides)

    pie_graph = go.Pie(labels=labels, values=values)
    fig = go.Figure(data=[pie_graph], layout=layout)

    img_bytes = fig.to_image(format='svg', engine='kaleido')
    return Response(img_bytes, mimetype='image/svg')


def test():

    return render_template('test_endpoint.html')
