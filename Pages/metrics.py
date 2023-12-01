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

external_stylesheets=[dbc.themes.BOOTSTRAP]

dash.register_page(__name__,external_stylesheets=external_stylesheets)


max_stations=summarystatistics.dataframe_max_stations()
max_bar_figure=px.bar(max_stations,x="Year",y="Value",color="Station")
max_bar_figure.update_layout(width=650,height=350,template="plotly_dark")

monthly_percent_change=summarystatistics.dataframe_monthly_percent_change()
monthly_percent_change_line_chart=px.line(monthly_percent_change,x="Period",y="Values")
monthly_percent_change_line_chart.update_layout(width=650,height=350,template="plotly_dark")

layout=html.Div([

    dbc.Row(dbc.Col(html.H1("Metrics Page"))),

    dbc.Row(
        [
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Title",className="card-text"),
                    html.H2(children="TEXT",className="card-text"), 
                ]),
            color="dark"
            )
        ),
                dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Title One",className="card-text"),
                    html.H2(children="TEXT One",className="card-text"), 
                ]),
            color="dark"
            )
        ),
        ]
    ),

    dbc.Row(
        [
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Title",className="card-text"),
                    html.H2(children="TEXT",className="card-text"), 
                ]),
            color="dark"
            )
        ),
                dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Title One",className="card-text"),
                    html.H2(children="TEXT One",className="card-text"), 
                ]),
            color="dark"
            )
        ),
        ]
    ),


    dbc.Row(
        [
        dbc.Col(html.H2("Max Ridership Per Year"),width=5), 
        dbc.Col(html.H2("Monthly Ridership Change"),width=7), 
         ]
    ),

        dbc.Row(
        [
        dbc.Col(dcc.Graph(figure=max_bar_figure),width=5), 
        dbc.Col(dcc.Graph(figure=monthly_percent_change_line_chart),width=5), 
         ]
    ),




])






"""layout=dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(children="Metrics Page"),
        ])
    ]),

    dbc.Row([
        dbc.Card(
            dbc.CardBody([
            html.H1(children="Max Ridership Per Year"),
            dcc.Graph(figure=max_bar_figure),
            ])

        )

        ],width=5),
        
        
        dbc.Col([
            
            html.H1(children="Percentage Change In Monthly Ridership"),
            dcc.Graph(figure=monthly_percent_change_line_chart),
       
        ])
    
    
    ])"""

