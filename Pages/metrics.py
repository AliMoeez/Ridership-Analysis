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
summarystatistics.dataframe_max_stations()

ttest=TTest()
ttest.customer_day_vs_hours_per_day()
ttest.customer_day_vs_km_per_day()
ttest.customer_day_vs_average_daily_vehicles()
ttest.graphs()

dash.register_page(__name__)

layout=html.Div([
    html.H2(children="Metrics Page",style={"textAlign":"center"}),
   
    html.H2(html.Span("Max Ridership Per Year"),className='divBorder'),

    dcc.Dropdown(id="MaxDropDown",options=["2022","2021","2020","2019"]),

    dcc.Graph(id="MaxGraph"),

])

@callback(
        Output("MaxGraph","figure"),
        Input("MaxDropDown","value")
)

def show_max_stations(year):
    max_stations=summarystatistics.dataframe_max_stations()
    figure=px.bar(max_stations,x="Year",y="Value",color="Station")
    return figure
    