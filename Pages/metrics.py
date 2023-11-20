import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import plotly.express as px

from Analysis.Summary_Statistics import SummaryStatistics
from Analysis.T_Test import TTest

summarystatistics=SummaryStatistics()
summarystatistics.busiest_station_2022()
summarystatistics.quietest_station_2022()
summarystatistics.busiest_month()
summarystatistics.quietest_month()
summarystatistics.busiest_station_per_year()

ttest=TTest()
ttest.customer_day_vs_hours_per_day()
ttest.customer_day_vs_km_per_day()
ttest.customer_day_vs_average_daily_vehicles()
ttest.graphs()

dash.register_page(__name__)

layout=html.Div([
    html.H2(children="Metrics Page",style={"textAlign":"center"}),

    html.Div(
        children=[html.H2("2022 Max")],
        style={"display":"inline-block","width":"25%"},className='divBorder'),

    html.Div(
        children=[html.H2("2021 Max")],
        style={"display":"inline-block","width":"25%"},className='divBorder'), 

    html.Div(
        children=[html.H2("2020 Max")],
        style={"display":"inline-block","width":"25%"},className='divBorder'),

    html.Div(
        children=[html.H2("2019 Max")],
        style={"display":"inline-block","width":"25%"},className='divBorder'),

])