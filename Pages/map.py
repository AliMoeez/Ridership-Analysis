import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import dash_bootstrap_components as dbc
import plotly.express as px

from Analysis.map_analysis import Map

external_stylesheets=[dbc.themes.BOOTSTRAP]

map_data=Map()
map_data.max_min_stations()
map_data.distance()

map_df=map_data.data()

map_analysis=map_data.map_other_data()

rounded_station_distance=round(map_analysis["Average Distance Between Stations"][0],2) 

map_figure=px.scatter_mapbox(map_df,lat="Latitude",lon="Longitude",
                             color="Station Name",size="Ridership (2014 Daily Average)",
                             color_continuous_scale=px.colors.cyclical.IceFire,size_max=15,zoom=10,mapbox_style="carto-positron")
map_figure.update_layout(template="plotly_dark",font_color="#FFFFFF")

dash.register_page(__name__,external_stylesheets=external_stylesheets)



layout=html.Div([

    html.H2(children="Map Page",style={"textAlign":"center"}),

    dbc.Row([
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Number of Stations",style={"textAlign":"center"}),
                    html.H3(children=map_analysis["Number of Stations"],style={"textAlign":"center"})
                ]),
            color="dark"
            )
        ),


        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Most Riders",style={"textAlign":"center"}),
                    html.H3(children=map_analysis["Most Riders"],style={"textAlign":"center"})
                ]),
            color="dark"
            )
        ),


        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Least Riders",style={"textAlign":"center"}),
                    html.H3(children=map_analysis["Least Riders"],style={"textAlign":"center"})
                ]),
            color="dark"
            )
        ),


        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Average Station Distance",style={"textAlign":"center"}),
                    html.H3(children=f'{rounded_station_distance} km',style={"textAlign":"center"})
                ]),
            color="dark"
            )
        ),
        
    ]),

    html.H2(children=""),


    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Graph(figure=map_figure)
                ]),
            color="dark"
            )
        )

    ]),



])