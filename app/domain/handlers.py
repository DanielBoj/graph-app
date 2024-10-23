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
common_size = dict(width=350)

def city_key_enrollment_pie_chart():

    payload = request.get_json()
    total_enrollment = int(payload['totalEnrollment'])
    total_citizens = int(payload['totalCitizens'])
    not_enrolled = total_citizens - total_enrollment

    labels = [config['label']['enrolled'], config['label']['not_enrolled']]
    values = [total_enrollment, not_enrolled]

    fig = px.pie(names=labels, values=values, title=config['title']['city_key_enrollment_pie_chart_title'])
    fig.update_layout(template=plotly_template, **common_size)
    
    graphs_list = [fig.to_json()]
    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def bus_year_rides_pie_chart():

    payload = request.get_json()
    total_rides = payload.get('totalRides', 0)
    in_year_rides = payload.get('inYearRides', 0)
    total_registered = payload.get('totalRegistered', 0)
    total_not_registered = payload.get('totalNotRegistered', 0)
    total_fisical_card = payload.get('totalFisicalCardRides', 0)
    total_virtual_card = payload.get('totalVirtualCardRides', 0)


    # 1st Pie Chart -> Total Bus Rides and InYear Bus Rides
    labels1 = [config['label']['total_bus_rides'], config['label']['in_year_bus_rides']]
    values1 = [total_rides, in_year_rides]

    year_pie_fig = px.pie(names=labels1, values=values1, title=config['title']['bus_year_rides_pie_chart_title'])
    year_pie_fig.update_layout(template=plotly_template, **common_size)

    # 2nd Pie Chart -> Registered and Not Registered Bus Rides
    labels2 = [config['label']['in_year_registered_bus_rides'], config['label']['in_year_not_registered_rides']]
    values2 = [total_registered, total_not_registered]

    registered_pie_fig = px.pie(names=labels2, values=values2, title=config['title']['bus_year_registered_rides_pie_chart_title'])
    registered_pie_fig.update_layout(template=plotly_template, **common_size)

    # 3rd Pie Chart -> Fisical and Virtual Card Bus Rides
    labels3 = [config['label']['fisical_card_bus_rides'], config['label']['virtual_card_bus_rides']]
    values3 = [total_fisical_card, total_virtual_card]

    card_type_pie_fig = px.pie(names=labels3, values=values3, title=config['title']['bus_year_fisical_and_virtual_card_rides_pie_chart_title'])
    card_type_pie_fig.update_layout(template=plotly_template, **common_size)

    graphs_list = [
        year_pie_fig.to_json(), 
        registered_pie_fig.to_json(), 
        card_type_pie_fig.to_json()
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def annual_bus_rides_bar_chart():

    actual_year = datetime.date.today().year

    payload = request.get_json()
    rides = payload['rides']

    years = [str(actual_year - len(rides) + i + 1) for i in range(len(rides))]
    values = [int(ride) for ride in rides]

    fig = px.bar(x=years, y=values, title=config['title']['annual_bus_rides_bar_chart_title'])
    fig.update_layout(
        template=plotly_template, 
        xaxis_title='Año', 
        yaxis_title='Viajes',
        **common_size
        )
    
    graphs_list = [fig.to_json()]
    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def monthly_bus_rides_bar_chart():

    payload = request.get_json()
    rides = payload['rides']

    month_names = list(calendar.month_abbr)[1:]
    values = [int(ride) for ride in rides]

    fig = px.bar(x=month_names, y=values, title=config['title']['monthly_bus_rides_bar_chart_title'])
    fig.update_layout(
        template=plotly_template, 
        xaxis_title='Mes', 
        yaxis_title='Viajes',
        **common_size
        )
    
    graphs_list = [fig.to_json()]
    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def daily_by_month_bus_rides_bar_chart():

    payload = request.get_json()
    rides = payload['rides']

    days_of_the_month = [str(i) for i in range(1, len(rides) + 1)]
    values = [int(ride) for ride in rides]

    fig = px.bar(x=days_of_the_month, y=values, title=config['title']['daily_by_month_bus_rides_bar_chart_title'])
    fig.update_layout(
        template=plotly_template,
        xaxis_title='Día del mes',
        yaxis_title='Viajes',
        **common_size
        )
    
    graphs_list = [fig.to_json()]
    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def weekly_bus_rides_bar_chart():

    payload = request.get_json()
    rides = payload['rides']
    limited_rides = rides[:7]

    days_of_the_week_names = list(calendar.day_abbr)[1:]
    values = [int(ride) for ride in limited_rides]

    fig = px.bar(x=days_of_the_week_names, y=values, title=config['title']['weekly_bus_rides_bar_chart_title'])
    fig.update_layout(
        template=plotly_template, 
        xaxis_title='Día de la semana', 
        yaxis_title='Viajes'
        **common_size
        )
    
    graphs_list = [fig.to_json()]
    return render_template('multiple_graphs_view.html', graphs=graphs_list)


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
        yaxis_title='Viajes',
        **common_size
        )

    graphs_list = [fig.to_json()]
    return render_template('multiple_graphs_view.html', graphs=graphs_list)	


def test():

    return render_template('test_endpoint.html')
