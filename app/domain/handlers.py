from plotly import express as px
from plotly import graph_objs as go
import pandas as pd
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

    """
    file: ../swagger/post_enrollment.yml
    """

    payload = request.get_json()
    total_registered_enrollments = payload.get('totalYearRegisteredEnrollments', 0)
    total_not_registered_enrollments = payload.get('totalYearNotRegisteredEnrollments', 0)

    # 1st Pie Chart -> Total Registered and Not Registered Enrollments
    labels1 = [config['label']['registered'], config['label']['not_registered']]
    values1 = [total_registered_enrollments, total_not_registered_enrollments]

    total_pie_fig = px.pie(names=labels1, values=values1, title=config['title']['city_key_enrollment_pie_chart_title'])
    total_pie_fig.update_traces(textinfo='value', hovertemplate='%{value}')
    total_pie_fig.add_annotation(
        text=f"Total: {total_registered_enrollments + total_not_registered_enrollments}",
        showarrow=False,
        x=0.1,
        y=0.0
    )

    total_pie_fig.update_layout(template=plotly_template)
    
    graphs_list = [
        total_pie_fig.to_json(), 
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def in_year_monthly_enrollments():

    payload = request.get_json()
    yearly_enrollment = payload['yearlyEnrollment']
    while len(yearly_enrollment) < 12:
        yearly_enrollment.append(0)

    month_names = months['es']
    values2 = [int(enrollment) for enrollment in yearly_enrollment]

    yearly_bar_fig = px.bar(x=month_names, y=values2, title=config['title']['city_key_yearly_enrollment_bar_chart_title'])
    yearly_bar_fig.update_layout(
        template=plotly_template, 
        xaxis_title='Mes', 
        yaxis_title='Inscripciones'
        )
    
    graphs_list = [
        yearly_bar_fig.to_json()
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def in_month_daily_enrollments():

    payload = request.get_json()
    monthly_enrollment = payload['monthlyEnrollment']

    days_of_the_month = [str(i) for i in range(1, len(monthly_enrollment) + 1)]
    values3 = [int(enrollment) for enrollment in monthly_enrollment]

    monthly_bar_fig = px.bar(x=days_of_the_month, y=values3, title=config['title']['city_key_daily_enrollment_bar_chart_title'])
    monthly_bar_fig.update_layout(
        template=plotly_template, 
        xaxis_title='Día del mes', 
        yaxis_title='Inscripciones'
        )
    
    graphs_list = [
        monthly_bar_fig.to_json()
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def weekly_enrollments():

    payload = request.get_json()
    weekly_enrollment = payload['weeklyEnrollment']
    while len(weekly_enrollment) < 7:
        weekly_enrollment.append(0)

    days_of_the_week = days['es']
    values4 = [int(enrollment) for enrollment in weekly_enrollment]

    weekly_bar_fig = px.bar(x=days_of_the_week, y=values4, title=config['title']['city_key_weekly_enrollment_bar_chart_title'])
    weekly_bar_fig.update_layout(
        template=plotly_template, 
        xaxis_title='Día de la semana', 
        yaxis_title='Inscripciones'
        )
    
    graphs_list = [
        weekly_bar_fig.to_json()
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def daily_enrollments():

    payload = request.get_json()

    daily_enrollment = payload['dailyEnrollment']

    day_hours = [f"{hour:02d}h" for hour in range(24)]
    values5 = [int(daily_enrollment[i]) if i < len(daily_enrollment) else 0 for i in range(24)]

    day_bar_fig = px.bar(x=day_hours, y=values5, title=config['title']['city_key_dayly_enrollment_bar_chart_title'])
    day_bar_fig.update_layout(
        template=plotly_template, 
        xaxis_title='Hora', 
        yaxis_title='Inscripciones'
        )
    
    graphs_list = [
        day_bar_fig.to_json()
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def recharges_and_bonus_uses_graphs():

    """
    file: ../swagger/post_purchases.yml
    """

    payload = request.get_json()
    total_monthly_purchases = payload['monthlyPurchases']

    month_names = months['es']
    values1 = [int(purchase) for purchase in total_monthly_purchases]

    monthly_bar_fig = px.bar(x=month_names, y=values1, title=config['title']['monthly_recharges_and_bonus_uses_bar_chart_title'])
    monthly_bar_fig.update_layout(
        template=plotly_template, 
        xaxis_title='Mes', 
        yaxis_title='Recargas y usos de bono'
        )
    
    
    
    graphs_list = [
        monthly_bar_fig.to_json(), 
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def daily_by_month_recharges_and_bonus_uses():

    payload = request.get_json()
    total_daily_by_month_purchases = payload['dailyByMonthPurchases']

    days_of_the_month = [str(i) for i in range(1, len(total_daily_by_month_purchases) + 1)]
    values2 = [int(purchase) for purchase in total_daily_by_month_purchases]

    daily_by_month_bar_fig = px.bar(x=days_of_the_month, y=values2, title=config['title']['daily_by_month_recharges_and_bonus_uses_bar_chart_title'])
    daily_by_month_bar_fig.update_layout(
        template=plotly_template, 
        xaxis_title='Día del mes', 
        yaxis_title='Recargas y usos de bono'
        )
    
    graphs_list = [
        daily_by_month_bar_fig.to_json
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def weekly_recharges_and_bonus_uses():

    payload = request.get_json()
    total_weekly_purchases = payload['weeklyPurchases']
    
    days_of_the_week = days['es']
    values3 = [int(purchase) for purchase in total_weekly_purchases]

    weekly_bar_fig = px.bar(x=days_of_the_week, y=values3, title=config['title']['weekly_recharges_and_bonus_uses_bar_chart_title'])
    weekly_bar_fig.update_layout(
        template=plotly_template, 
        xaxis_title='Día de la semana', 
        yaxis_title='Recargas y usos de bono'
        )
    
    graphs_list = [
        weekly_bar_fig.to_json()
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def daily_recharges_and_bonus_uses():

    payload = request.get_json()
    total_daily_purchases = payload['dailyPurchases']
    
    day_hours = [f"{hour:02d}h" for hour in range(24)]
    values4 = [int(total_daily_purchases[i]) if i < len(total_daily_purchases) else 0 for i in range(24)]

    daily_bar_fig = px.bar(x=day_hours, y=values4, title=config['title']['daily_recharges_and_bonus_uses_bar_chart_title'])
    daily_bar_fig.update_layout(
        template=plotly_template, 
        xaxis_title='Hora', 
        yaxis_title='Recargas y usos de bono'
        )
    
    graphs_list = [
        daily_bar_fig.to_json()
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def courses_and_workshops_graphs():

    """
    file: ../swagger/post_courses.yml
    """

    payload = request.get_json()
    total_ended_courses = payload.get('totalEndedCourses', 0)
    total_on_going_courses = payload.get('totalOnCurseCourses', 0)
    total_year_payed_courses = payload.get('totalYearPayedCourses', 0)
    total_year_free_courses = payload.get('totalYearFreeCourses', 0)

    # 1st Pie Chart -> Ended and On Going Courses
    labels = [config['label']['ended_courses'], config['label']['on_going_courses']]
    values = [total_ended_courses, total_on_going_courses]

    course_pie_fig = px.pie(names=labels, values=values, title=config['title']['courses_and_workshops_status_pie_chart_title'])
    course_pie_fig.update_traces(textinfo='value', hovertemplate='%{value}')
    course_pie_fig.add_annotation(
        text=f"Total: {total_ended_courses + total_on_going_courses}",
        showarrow=False,
        x=0.1,
        y=0.0
    )
    course_pie_fig.update_layout(template=plotly_template)

    # 2nd Pie Chart -> Total Payed and Free Courses
    labels1 = [config['label']['payed_courses'], config['label']['free_courses']]
    values1 = [total_year_payed_courses, total_year_free_courses]

    total_pie_fig = px.pie(names=labels1, values=values1, title=config['title']['courses_and_workshops_pie_chart_title'])
    total_pie_fig.update_traces(textinfo='value', hovertemplate='%{value}')
    total_pie_fig.add_annotation(
        text=f"Total: {total_year_payed_courses + total_year_free_courses}",
        showarrow=False,
        x=0.1,
        y=0.0
    )
    total_pie_fig.update_layout(template=plotly_template)
    
    graphs_list = [
        course_pie_fig.to_json(),
        total_pie_fig.to_json(),
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def yearly_courses_bar_chart():

    payload = request.get_json()
    yearly_by_month_payed_courses = payload['yearlyByMonthPayedCourses']
    yearly_by_month_free_courses = payload['yearlyByMonthFreeCourses']

    month_names = months['es']
    values2 = [int(course) for course in yearly_by_month_payed_courses]
    values3 = [int(course) for course in yearly_by_month_free_courses]

    df = pd.DataFrame({
        'Mes': month_names,
        'Cursos y talleres pagados': values2,
        'Cursos y talleres gratuitos': values3
    })

    yearly_bar_fig = px.bar(df, x='Mes', y=['Cursos y talleres pagados', 'Cursos y talleres gratuitos'], title=config['title']['courses_and_workshops_yearly_bar_chart_title'])
    yearly_bar_fig.update_layout(
        template=plotly_template,
        xaxis_title='Mes',
        yaxis_title='Cursos y talleres'
    )

    graphs_list = [
        yearly_bar_fig.to_json()
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def monthly_courses_bar_chart():

    payload = request.get_json()
    monthly_by_day_payed_courses = payload['monthlyByDayPayedCourses']
    monthly_by_day_free_courses = payload['monthlyByDayFreeCourses']

    days_of_the_month = [str(i) for i in range(1, len(monthly_by_day_payed_courses) + 1)]
    values4 = [int(course) for course in monthly_by_day_payed_courses]
    values5 = [int(course) for course in monthly_by_day_free_courses]

    df = pd.DataFrame({
        'Día del mes': days_of_the_month,
        'Cursos y talleres pagados': values4,
        'Cursos y talleres gratuitos': values5
    })

    monthly_bar_fig = px.bar(df, x='Día del mes', y=['Cursos y talleres pagados', 'Cursos y talleres gratuitos'], title=config['title']['courses_and_workshops_monthly_bar_chart_title'])
    monthly_bar_fig.update_layout(
        template=plotly_template,
        xaxis_title='Día del mes',
        yaxis_title='Cursos y talleres'
    )

    graphs_list = [
        monthly_bar_fig.to_json()
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def weekly_courses_bar_chart():   

    payload = request.get_json()
    weekly_payed_courses = payload['weeklyPayedCourses']
    weekly_free_courses = payload['weeklyFreeCourses']

    days_of_the_week = days['es']
    values6 = [int(course) for course in weekly_payed_courses]
    values7 = [int(course) for course in weekly_free_courses]

    df = pd.DataFrame({
        'Día de la semana': days_of_the_week,
        'Cursos y talleres pagados': values6,
        'Cursos y talleres gratuitos': values7
    })

    weekly_bar_fig = px.bar(df, x='Día de la semana', y=['Cursos y talleres pagados', 'Cursos y talleres gratuitos'], title=config['title']['courses_and_workshops_weekly_bar_chart_title'])
    weekly_bar_fig.update_layout(
        template=plotly_template,
        xaxis_title='Día de la semana',
        yaxis_title='Cursos y talleres'
    )

    graphs_list = [
        weekly_bar_fig.to_json()
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)
    

def daily_courses_bar_chart():

    payload = request.get_json()
    daily_payed_courses = payload['dailyPayedCourses']
    daily_free_courses = payload['dailyFreeCourses']

    day_hours = [f"{hour:02d}h" for hour in range(24)]
    values8 = [int(daily_payed_courses[i]) if i < len(daily_payed_courses) else 0 for i in range(24)]
    values9 = [int(daily_free_courses[i]) if i < len(daily_free_courses) else 0 for i in range(24)]

    df = pd.DataFrame({
        'Hora': day_hours,
        'Cursos y talleres pagados': values8,
        'Cursos y talleres gratuitos': values9
    })

    daily_bar_fig = px.bar(df, x='Hora', y=['Cursos y talleres pagados', 'Cursos y talleres gratuitos'], title=config['title']['courses_and_workshops_daily_bar_chart_title'])
    daily_bar_fig.update_layout(
        template=plotly_template,
        xaxis_title='Hora',
        yaxis_title='Cursos y talleres'
    )

    graphs_list = [
        daily_bar_fig.to_json()
    ]

    return render_template('multiple_graphs_view.html', graphs=graphs_list)


def bus_year_rides_pie_chart():

    """
    file: ../swagger/post_bus_total_year.yml
    """


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

    """
    file: ../swagger/post_bus_annual.yml
    """

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

    """
    file: ../swagger/post_bus_monthly.yml
    """

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

    """
    file: ../swagger/post_bus_daily_by_month.yml
    """

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

    """
    file: ../swagger/post_bus_weekly.yml
    """


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

    """
    file: ../swagger/post_bus_daily.yml
    """

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
