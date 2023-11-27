import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import dash_bootstrap_components as dbc
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


layout=dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(children="Metrics Page"),
        ])
    ]),

    dbc.Row([
        dbc.Col([
            
            html.H1(children="Max Ridership Per Year"),
            dcc.Graph(figure=max_bar_figure),

        ],width=5),
        
        
        dbc.Col([
            
            html.H1(children="Percentage Change In Monthly Ridership"),
            dcc.Graph(figure=monthly_percent_change_line_chart),
       
        ],justfity="left")
    
    
    
    ]),

    dbc.Row([
        dbc.Col([
            html.H1(children="Metrics Two")
        ],style={"display":"inline-block"}),
    ]),



])

"""layout=html.Div([
    html.H2(children="Metrics Page",style={"textAlign":"center"}),
   
    html.H2(children="Max Ridership Per Year",className='divBorder',style={"display":"inline-block"}),

    html.H2(children="THIS METRICS ",className='divBorder',style={"display":"inline-block"}),

    dcc.Graph(figure=max_bar_figure),

    html.H2(children="Percentage Change In Monthly Ridership",className='divBorder'),

    dcc.Graph(figure=monthly_percent_change_line_chart),

])"""

    