import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

from Analysis.Summary_Statistics import SummaryStatistics
from Analysis.T_Test import TTest

summarystatistics=SummaryStatistics()
summarystatistics.busiest_station_2022()
summarystatistics.quietest_station_2022()
busy_month=summarystatistics.busiest_month()
quiet_month=summarystatistics.quietest_month()
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
                    html.H2(children="Busiest Month",className="card-text"),
                    html.H2(children=f"{busy_month[2]} {busy_month[1]} : {busy_month[3]:,} average daily riders",className="card-text"), 
                ]),
            color="dark"
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Quietest Month",className="card-text"),
                    html.H2(children=f"{quiet_month[2]} {quiet_month[1]} : {quiet_month[3]:,} average daily riders",className="card-text"),
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
                    html.H2("Most Used Stations in 2022",className="card-text"),
                    dcc.Dropdown(id="T10SPY",options=["2022","2021","2020","2019"],value="2022"),
                    dcc.Graph(id="T10SPY Graph"),
                ]),
            color="dark"
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="AM & PM Peak Vechicles 2019-2022",className="card-text"),
                    dcc.Dropdown(id="AMPM",options=["Total","AM","PM"]),
                    dcc.Graph(id="AMPM Graph"),
                ]),
            color="dark"
            )
        ),
        ]
    ),


    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dbc.Col(html.H2("Max Ridership Per Year",className="card-text"),width=5), 
                    dbc.Col(dcc.Graph(figure=max_bar_figure,className="card-text")), 
                ]),
                color="dark", style={"width":700}
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dbc.Col(html.H2("Monthly Ridership Change",className="card-text"),width=5), 
                    dbc.Col(dcc.Graph(figure=monthly_percent_change_line_chart,className="card-text")), 
                ]),
                color="dark",style={"width":700}
        )

        )
    ]),



])


@callback(
    Output("T10SPY Graph","figure"),
    Input("T10SPY","value"),
  
)
def top_ten_stations_function(year):
    if year=="2022":
        print("HERE")
        top_stations=summarystatistics.top_ten_stations_2022()[0]
        top_stations_figure=px.bar(top_stations,x="Customers\nper day",y="Route",orientation="h")
        top_stations_figure.update_layout(width=650,height=350,template="plotly_dark",yaxis=dict(autorange="reversed"))
        return top_stations_figure
    elif year=="2021":
        top_stations=summarystatistics.top_ten_stations_2022()[1]
        top_stations_figure=px.bar(top_stations,x="Customers\nper day",y="Route",orientation="h")
        top_stations_figure.update_layout(width=650,height=350,template="plotly_dark",yaxis=dict(autorange="reversed"))
        return top_stations_figure
    elif year=="2020":
        top_stations=summarystatistics.top_ten_stations_2022()[2]
        top_stations_figure=px.bar(top_stations,x="Customers per day",y="Route",orientation="h")
        top_stations_figure.update_layout(width=650,height=350,template="plotly_dark",yaxis=dict(autorange="reversed"))
        return top_stations_figure
    elif year=="2019":
        top_stations=summarystatistics.top_ten_stations_2022()[3]
        top_stations_figure=px.bar(top_stations,x="Customers per day",y="Route",orientation="h")
        top_stations_figure.update_layout(width=650,height=350,template="plotly_dark",yaxis=dict(autorange="reversed"))
        return top_stations_figure
    

@callback(
    Output("AMPM Graph","figure"),
    Input("AMPM","value")
)

def max_figure_function(years):
    if years=="AM":
        print("HERE")
        max_vechicles=summarystatistics.am_vehicle_peak()
        max_vechicles_line_chart=px.line(max_vechicles,x="Year",y="Value")
        max_vechicles_line_chart.update_layout(width=650,height=350,template="plotly_dark")
        return max_vechicles_line_chart
    elif years=="PM":
        max_vechicles=summarystatistics.pm_vehicle_peak()
        max_vechicles_line_chart=px.line(max_vechicles,x="Year",y="Value")
        max_vechicles_line_chart.update_layout(width=650,height=350,template="plotly_dark")
        return max_vechicles_line_chart
    else:
        max_vechicles_am=summarystatistics.am_vehicle_peak()
        max_vechicles_pm=summarystatistics.pm_vehicle_peak()
        
        max_vechicles_line_chart_am=px.line(max_vechicles_am,x="Year",y="Value")
        max_vechicles_line_chart_pm=px.line(max_vechicles_pm,x="Year",y="Value")

        max_vechicles_line_chart=go.Figure(data=max_vechicles_line_chart_am.data+max_vechicles_line_chart_pm.data)


        max_vechicles_line_chart.update_layout(width=650,height=350,template="plotly_dark")  
        return max_vechicles_line_chart     




