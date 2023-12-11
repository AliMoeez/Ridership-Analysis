import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import plotly.express as px

from Analysis.map_analysis import Map

map_data=Map()

map_df=map_data.data()

map_figure=px.scatter_mapbox(map_df,lat="Latitude",lon="Longitude",
                             color="Station Name",size="Ridership (2014 Daily Average)",
                             color_continuous_scale=px.colors.cyclical.IceFire,size_max=15,zoom=10,mapbox_style="carto-positron")
map_figure.update_layout(template="plotly_dark",font_color="#FFFFFF")

dash.register_page(__name__)

layout=html.Div([
    html.H2(children="Map Page",style={"textAlign":"center"}),

    dcc.Graph(figure=map_figure)


])