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
summarystatistics.dataframe_monthly_percent_change()

ttest=TTest()
ttest.customer_day_vs_hours_per_day()
ttest.customer_day_vs_km_per_day()
ttest.customer_day_vs_average_daily_vehicles()
ttest.graphs()

dash.register_page(__name__)

max_stations=summarystatistics.dataframe_max_stations()
max_bar_figure=px.bar(max_stations,x="Year",y="Value",color="Station")
max_bar_figure.update_layout(width=650,height=350,template="plotly_dark")

monthly_percent_change=summarystatistics.dataframe_monthly_percent_change()
monthly_percent_change_line_chart=px.line(monthly_percent_change,x="Period",y="Values")
monthly_percent_change_line_chart.update_layout(width=650,height=350,template="plotly_dark")

layout=html.Div([
    html.H2(children="Metrics Page",style={"textAlign":"center"}),
   
    html.H2(html.Span("Max Ridership Per Year"),className='divBorder'),

    dcc.Graph(figure=max_bar_figure),

    dcc.Graph(figure=monthly_percent_change_line_chart),

])

    