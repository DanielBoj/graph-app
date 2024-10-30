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

def city_key_enrollment_graphs():

    payload = request.get_json()
    total_registered_enrollments = payload.get('totalYearRegisteredEnrollments', 0)
    total_not_registered_enrollments = payload.get('totalYearNotRegisteredEnrollments', 0)

    yearly_enrollment = payload['yearlyEnrollment']
    while len(yearly_enrollment) < 12:
        yearly_enrollment.append(0)

    monthly_enrollment = payload['monthlyEnrollment']

    weekly_enrollment = payload['weeklyEnrollment']
    while len(weekly_enrollment) < 7:
        weekly_enrollment.append(0)

    daily_enrollment = payload['dailyEnrollment']

    # 1st Pie Chart -> Total Enrollments and Not Enrollments
    labels1 = [config['label']['registered'], config['label']['not_registered']]
    values1 = [total_registered_enrollments, total_not_registered_enrollments]

    total_pie_fig = px.pie(names=labels1, values=values1, title=config['title']['city_key_enrollment_pie_chart_title'])
    total_pie_fig.update_traces(textinfo='value', hovertemplate='%{value}')
    total_pie_fig.add_annotation(
        text=f"Total: {total_registered_enrollments + total_not_registered_enrollments}",
        showarrow=False,
        x=0.75,
        y=0.0
    )

    total_pie_fig.update_layout(template=plotly_template)

    # 2nd Bar Chart -> In year monthly enrollments
    month_names = months['es']
    values2 = [int(enrollment) for enrollment in yearly_enrollment]

    yearly_bar_fig = px.bar(x=month_names, y=values2, title=config['title']['city_key_yearly_enrollment_bar_chart_title'])
    yearly_bar_fig.update_layout(
        template=plotly_template, 
        xaxis_title='Mes', 
        yaxis_title='Inscripciones'
        )
    
    # 3rd Bar Chart -> In month daily enrollments
    days_of_the_month = [str(i) for i in range(1, len(monthly_enrollment) + 1)]
    values3 = [int(enrollment) for enrollment in monthly_enrollment]

    monthly_bar_fig = px.bar(x=days_of_the_month, y=values3, title=config['title']['city_key_daily_enrollment_bar_chart_title'])
    monthly_bar_fig.update_layout(
        template=plotly_template, 
        xaxis_title='Día del mes', 
        yaxis_title='Inscripciones'
        )
    
    # 4th Bar Chart -> In week daily enrollments
    days_of_the_week = days['es']
    values4 = [int(enrollment) for enrollment in weekly_enrollment]

    weekly_bar_fig = px.bar(x=days_of_the_week, y=values4, title=config['title']['city_key_weekly_enrollment_bar_chart_title'])
    weekly_bar_fig.update_layout(
        template=plotly_template, 
        xaxis_title='Día de la semana', 
        yaxis_title='Inscripciones'
        )
    
    # 5th Bar Chart -> In day enrollment
    day_hours = [f"{hour:02d}h" for hour in range(24)]
    values5 = [int(daily_enrollment[i]) if i < len(daily_enrollment) else 0 for i in range(24)]

    day_bar_fig = px.bar(x=day_hours, y=values5, title=config['title']['city_key_dayly_enrollment_bar_chart_title'])
    day_bar_fig.update_layout(
        template=plotly_template, 
        xaxis_title='Hora', 
        yaxis_title='Inscripciones'
        )
    
    graphs_list = [
        total_pie_fig.to_json(), 
        yearly_bar_fig.to_json(), 
        monthly_bar_fig.to_json(), 
        weekly_bar_fig.to_json(), 
        day_bar_fig.to_json()
    ]

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
    year_pie_fig.update_layout(template=plotly_template)

    # 2nd Pie Chart -> Registered and Not Registered Bus Rides
    labels2 = [config['label']['in_year_registered_bus_rides'], config['label']['in_year_not_registered_rides']]
    values2 = [total_registered, total_not_registered]

    registered_pie_fig = px.pie(names=labels2, values=values2, title=config['title']['bus_year_registered_rides_pie_chart_title'])
    registered_pie_fig.update_layout(template=plotly_template)

    # 3rd Pie Chart -> Fisical and Virtual Card Bus Rides
    labels3 = [config['label']['fisical_card_bus_rides'], config['label']['virtual_card_bus_rides']]
    values3 = [total_fisical_card, total_virtual_card]

    card_type_pie_fig = px.pie(names=labels3, values=values3, title=config['title']['bus_year_fisical_and_virtual_card_rides_pie_chart_title'])
    card_type_pie_fig.update_layout(template=plotly_template)

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
        yaxis_title='Viajes'
        )
    
    graphs_list = [fig.to_json()]
    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def monthly_bus_rides_bar_chart():

    payload = request.get_json()
    rides = payload['rides']

    while len(rides) < 12:
        rides.append(0)

    if locale.getlocale()[0] == 'es_ES':
        month_names = short_months['es']
    else:
        month_names = short_months['en']
    values = [int(ride) for ride in rides]

    fig = px.bar(x=month_names, y=values, title=config['title']['monthly_bus_rides_bar_chart_title'])
    fig.update_layout(
        template=plotly_template, 
        xaxis_title='Mes', 
        yaxis_title='Viajes'
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
        yaxis_title='Viajes'
        )
    
    graphs_list = [fig.to_json()]
    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def weekly_bus_rides_bar_chart():

    payload = request.get_json()
    rides = payload['rides']
    limited_rides = rides[:7]

    while len(limited_rides) < 7:
        limited_rides.append(0)

    if locale.getlocale()[0] == 'es_ES':
        days_of_the_week_names = days['es']
    else:
        days_of_the_week_names = days['en']
    values = [int(ride) for ride in limited_rides]

    fig = px.bar(x=days_of_the_week_names, y=values, title=config['title']['weekly_bus_rides_bar_chart_title'])
    fig.update_layout(
        template=plotly_template, 
        xaxis_title='Día de la semana', 
        yaxis_title='Viajes'
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
        yaxis_title='Viajes'
        )

    graphs_list = [fig.to_json()]
    return render_template('multiple_graphs_view.html', graphs=graphs_list)	


days = {
    'es': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
    'en': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
}

months = {
    'es': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
}

short_months = {
    'es': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
    'en': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
}


def test():

    return render_template('test_endpoint.html')
