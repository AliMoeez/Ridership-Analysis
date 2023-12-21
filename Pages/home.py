import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import dash_bootstrap_components as dbc
import plotly.express as px

external_stylesheets=[dbc.themes.BOOTSTRAP]

dash.register_page(__name__,path="/",external_stylesheets=external_stylesheets)

layout=html.Div([
    dbc.Row(dbc.Col(html.H2(children="Home Page",style={"textAlign":"center"}))),


    html.H2(children=""),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2("Welcome To The TTC Ridership Analysis Dashboard!",style={"textAlign":"center"}),
                    html.H3("Here you will find analysis and vizulizations of TTC Data",style={"textAlign":"center"})
                ]),
            color="dark"
            )
        )
    ]),

    html.H2(children=""),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2("Use The Links Above To Navigate To Your Desired Page",style={"textAlign":"center"}),
                    html.H3("Links Include : TTC Map, TTC Metrics & A Neural Network Made of TTC Ridership Data",style={"textAlign":"center"})
                ]),
            color="dark"
            )
        )
    ]),

    html.H2(children=""),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2("Thank you for using the Dashboard!",style={"textAlign":"center"}),
                ]),
            color="dark"
            )
        )
    ]),




])