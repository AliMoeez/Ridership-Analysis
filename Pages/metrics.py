import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import plotly.express as px

dash.register_page(__name__)

layout=html.Div([
    html.H2(children="Metrics Page",style={"textAlign":"center"})

])