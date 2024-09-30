from plotly import graph_objs as go
from flask import Response, request, render_template
import datetime
import calendar
import locale

from configuration.config_loader import config

import plotly.io as pio
pio.kaleido.scope.default_format = 'svg'
pio.kaleido.scope.default_scale = 2

locale.setlocale(
    category=locale.LC_ALL, 
    locale=''
    )


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
    
    img_bytes = fig.to_image(format='svg', engine='kaleido', scale=3)
    return Response(img_bytes, mimetype='media/svg')

def bus_year_rides_pie_chart():

    payload = request.get_json()
    total_rides = int(payload['totalRides'])
    in_year_rides = int(payload['inYearRides'])

    labels = [config['label']['total_bus_rides'], config['label']['in_year_bus_rides']]
    values = [total_rides, in_year_rides]

    layout = go.Layout(title=config['title']['bus_year_rides_pie_chart_title'])

    pie_graph = go.Pie(labels=labels, values=values)
    fig = go.Figure(data=[pie_graph], layout=layout)

    img_bytes = fig.to_image(format='svg', engine='kaleido', scale=3)
    return Response(img_bytes, mimetype='image/svg')

def bus_year_registered_rides_pie_chart():

    payload = request.get_json()
    total_registered_rides = int(payload['totalRegisteredRides'])
    in_year_registered_rides = int(payload['inYearRegisteredRides'])

    labels = [config['label']['total_registered_bus_rides'], config['label']['in_year_registered_bus_rides']]
    values = [total_registered_rides, in_year_registered_rides]

    layout = go.Layout(title=config['title']['bus_year_registered_rides_pie_chart_title'])

    pie_graph = go.Pie(labels=labels, values=values)
    fig = go.Figure(data=[pie_graph], layout=layout)

    img_bytes = fig.to_image(format='svg', engine='kaleido', scale=3)
    return Response(img_bytes, mimetype='image/svg')

def bus_year_fisical_and_virtual_card_rides_pie_chart():
    
    payload = request.get_json()
    total_fisical_card_rides = int(payload['totalFisicalCardRides'])
    total_virtual_card_rides = int(payload['totalVirtualCardRides'])

    labels = [config['label']['fisical_card_bus_rides'], config['label']['virtual_card_bus_rides']]
    values = [total_fisical_card_rides, total_virtual_card_rides]

    layout = go.Layout(title=config['title']['bus_year_fisical_and_virtual_card_rides_pie_chart_title'])

    pie_graph = go.Pie(labels=labels, values=values)
    fig = go.Figure(data=[pie_graph], layout=layout)

    img_bytes = fig.to_image(format='svg', engine='kaleido', scale=3)
    return Response(img_bytes, mimetype='image/svg')

def annual_bus_rides_bar_chart():

    actual_year = datetime.date.today().year

    payload = request.get_json()
    rides = payload['rides']

    years = [str(actual_year - len(rides) + i) for i in range(len(rides))]
    values = [int(ride) for ride in rides]

    layout = go.Layout(title=config['title']['annual_bus_rides_bar_chart_title'])

    bar_graph = go.Bar(x=years, y=values)
    fig = go.Figure(data=[bar_graph], layout=layout)

    img_bytes = fig.to_image(format='svg', engine='kaleido', scale=3)
    return Response(img_bytes, mimetype='image/svg')


def monthly_bus_rides_bar_chart():

    payload = request.get_json()
    rides = payload['rides']

    month_names = list(calendar.month_abbr)[1:]
    values = [int(ride) for ride in rides]

    layout = go.Layout(title=config['title']['monthly_bus_rides_bar_chart_title'])

    bar_graph = go.Bar(x=month_names, y=values)
    fig = go.Figure(data=[bar_graph], layout=layout)

    img_bytes = fig.to_image(format='svg', engine='kaleido', scale=3)
    return Response(img_bytes, mimetype='image/svg')

def daily_bus_rides_bar_chart():

    payload = request.get_json()
    rides = payload['rides']

    day_names = list(calendar.day_abbr)[1:]
    values = [int(ride) for ride in rides]

    layout = go.Layout(title=config['title']['dayly_bus_rides_bar_chart_title'])

    bar_graph = go.Bar(x=day_names, y=values)
    fig = go.Figure(data=[bar_graph], layout=layout)

    img_bytes = fig.to_image(format='svg', engine='kaleido', scale=3)
    return Response(img_bytes, mimetype='image/svg')


def test():

    return render_template('test_endpoint.html')
