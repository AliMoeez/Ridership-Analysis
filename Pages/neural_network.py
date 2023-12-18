import dash
from dash import Dash,html,dash_table,dcc,Input,Output,callback
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
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

data_value=neuralnetworkanalysis.model_inverse_transform_scale()[0]
data_prediction=neuralnetworkanalysis.model_inverse_transform_scale()[1]

external_stylesheets=[dbc.themes.BOOTSTRAP]

dash.register_page(__name__,external_stylesheets=external_stylesheets)

"""neural_network_figure_data=px.line(data_value,x="Month And Year",y="Value")
neural_network_figure_prediction=px.line(data_prediction,x="Month And Year",y="Prediction")
neural_network_figure_prediction['data'][0]['line']['color']="#FF0000"

neutal_network_figure=go.Figure(data=neural_network_figure_data.data+neural_network_figure_prediction.data)
neutal_network_figure.update_layout(template="plotly_dark")"""

neural_network_figure=make_subplots(rows=1,cols=1)
neural_network_figure.update_layout(template="plotly_dark")
neural_network_figure.append_trace(go.Scatter(x=data_value["Month And Year"],y=data_value["Value"],mode="lines",name="Original Data"),row=1,col=1)
neural_network_figure.append_trace(go.Scatter(x=data_prediction["Month And Year"],y=data_prediction["Prediction"],mode="lines",name="Neural Network Prediction"),row=1,col=1)


layout=html.Div([
    
    dbc.Row([dbc.Col(html.H2(children="Neural Network Page",style={"textAlign":"center"}))]),

    dbc.Row([ 
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Number of Epochs",style={"textAlign":"center"}),
                
                ]),
            color="dark"
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Mean Standard Error (MSE)",style={"textAlign":"center"}),
                
                ]),
            color="dark"
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Accuracy",style={"textAlign":"center"}),
                
                ]),
            color="dark"
            )
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children="Model Optimizer",style={"textAlign":"center"}),

                ]),
            color="dark"
            )
        ),

    ]),


    dbc.Row([
        dbc.Col(
            html.H2(children=""),
            
        )

    ]),


    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Graph(figure=neural_network_figure)

                ]),
            color="dark"
            )
        )

    ])

    

])