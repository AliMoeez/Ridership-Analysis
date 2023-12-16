import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc

from Analysis.Neural_Network_Anaylsis import NeuralNetworkAnalysis

neuralnetworkanalysis=NeuralNetworkAnalysis()
neuralnetworkanalysis.create_timeline()
neuralnetworkanalysis.transform_scale_numbers()
neuralnetworkanalysis.train_data()
neuralnetworkanalysis.data_into_array()
neuralnetworkanalysis.model()
neuralnetworkanalysis.model_compile()
neuralnetworkanalysis.model_predict()

month_and_year=neuralnetworkanalysis.model_inverse_transform_scale()[0]
data_value=neuralnetworkanalysis.model_inverse_transform_scale()[1]
data_prediction=neuralnetworkanalysis.model_inverse_transform_scale()[2]

external_stylesheets=[dbc.themes.BOOTSTRAP]

dash.register_page(__name__,external_stylesheets=external_stylesheets)

neural_network_figure_data=px.line(data_value,x=month_and_year,y=data_value)
neural_network_figure_prediction=px.line(data_prediction,x=month_and_year,y=data_prediction)

neutal_network_figure=go.Figure(data=neural_network_figure_data+neural_network_figure_prediction)


layout=html.Div([
    html.H2(children="Neural Network Page",style={"textAlign":"center"}),

    dbc.Row([ 
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="DATA 1",style={"textAlign":"center"}),
                
                ])
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="DATA 2",style={"textAlign":"center"}),
                
                ])
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="DATA 3",style={"textAlign":"center"}),
                
                ])
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="DATA 4",style={"textAlign":"center"}),
                
                ])
            )
        ),

    ]),


    dbc.Row([[ 
        dbc.Col(
            html.H2(children=""),
            
        )

    ]]),


    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Graph(figure=neutal_network_figure)

                ])
            )
        )





    ])

    

])