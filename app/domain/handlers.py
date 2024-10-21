from plotly import express as px
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

plotly_template = "seaborn"

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
    in_year_not_registered_rides = int(payload['inYearNotRegisteredRides'])
    in_year_registered_rides = int(payload['inYearRegisteredRides'])

    labels = [config['label']['in_year_not_registered_rides'], config['label']['in_year_registered_bus_rides']]
    values = [in_year_not_registered_rides, in_year_registered_rides]

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

    years = [str(actual_year - len(rides) + i + 1) for i in range(len(rides))]
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


def daily_by_month_bus_rides_bar_chart():

    payload = request.get_json()
    rides = payload['rides']

    days_of_the_month = [str(i) for i in range(1, len(rides) + 1)]
    values = [int(ride) for ride in rides]

    layout = go.Layout(title=config['title']['daily_by_month_bus_rides_bar_chart_title'])

    bar_graph = go.Bar(x=days_of_the_month, y=values)
    fig = go.Figure(data=[bar_graph], layout=layout)

    img_bytes = fig.to_image(format='svg', engine='kaleido', scale=3)
    return Response(img_bytes, mimetype='image/svg')


def weekly_bus_rides_bar_chart():

    payload = request.get_json()
    rides = payload['rides']
    limited_rides = rides[:7]

    days_of_the_week_names = list(calendar.day_abbr)[1:]
    values = [int(ride) for ride in limited_rides]

    layout = go.Layout(title=config['title']['weekly_bus_rides_bar_chart_title'])

    bar_graph = go.Bar(x=days_of_the_week_names, y=values)
    fig = go.Figure(data=[bar_graph], layout=layout)

    img_bytes = fig.to_image(format='svg', engine='kaleido', scale=3)
    return Response(img_bytes, mimetype='image/svg')


def daily_bus_rides_bar_chart():

    payload = request.get_json()
    rides = payload['rides']
    limited_rides = rides[:24]

    day_hours = [f"{hour:02d}h" for hour in range(24)]
    values = [int(limited_rides[i]) if i < len(limited_rides) else 0 for i in range(24)]

    fig = px.bar(x=day_hours, y=values, title=config['title']['dayly_bus_rides_bar_chart_title'])
    fig.update_layout(
        template=plotly_template, 
        xaxis_title='Hora', 
        yaxis_title='Viajes'
        )

    # layout = go.Layout(template=plotly_template, title=config['title']['dayly_bus_rides_bar_chart_title'])

    # bar_graph = go.Bar(x=day_hours, y=values)
    # fig = go.Figure(data=[bar_graph], layout=layout)
    graph_json = fig.to_json()

    # img_bytes = fig.to_image(format='svg', engine='kaleido', scale=3)
    graph_html = fig.to_html(full_html=False)
    # return Response(img_bytes, mimetype='image/svg')
    return render_template('graphs_view.html', graphs=graph_json)	


def test():

    return render_template('test_endpoint.html')
