import dash
from dash import Dash,html,dash_table,dcc,Input,Output
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

external_stylesheets=[dbc.themes.BOOTSTRAP]

app=Dash(__name__,use_pages=True,external_stylesheets=external_stylesheets)

app.layout=html.Div([
    
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H1(children="Toronto Transit Commision (TTC) Ridership Dashboard",style={"textAlign":"left"}),
                ]),
            color="dark"
            )
        )                       
    ]),

    html.H2(children=""),

    html.Div([
    html.Div(
        dcc.Link(f"{page['name'].title()}",href=page["relative_path"]),
        style={"width":"20%","display":"inline-block","textAlign":"center","fontWeight":"bold"}) 
    for page in dash.page_registry.values()
    ]),

    dash.page_container

])

if __name__=='__main__':
    app.run(debug=True)