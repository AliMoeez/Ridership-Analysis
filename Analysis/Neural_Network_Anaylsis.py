import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import RootMeanSquaredError
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

class NeuralNetworkAnalysis:
    def __init__(self) -> None:
        #Load the dataframe, and organize the data
        self.df=pd.read_excel(r"Data\Ridership_Data.xlsx",sheet_name=None)
        self.df_weekly_ridership=self.df["Weekly TTC Ridership Data"]
        self.df_weekly_ridership["Month And Year"]=self.df_weekly_ridership["Period"]+ " " +self.df_weekly_ridership["Year"].astype(str)

    def create_timeline(self):
        #Add Timeline to sucesfully run the Neural Network
        self.time_line=[] ; self.time=0
        for i in range(len(self.df_weekly_ridership["Value"])):
            self.time+=1 ; self.time_line.append(self.time)

    def transform_scale_numbers(self):
        #Transform Numbers to allow for better Neural Network Results And Predictions
        #Numbers use the 0-1 scale
        self.scaler=MinMaxScaler((0,1))
        self.df_weekly_ridership["Value"]=self.scaler.fit_transform(self.df_weekly_ridership[["Value"]])

    def train_data(self):
        #Define The Training Data
        self.train_data=self.df_weekly_ridership["Value"] 

    def data_into_array(self):
        #Create datsasets where one dataset looks 10 points in the points, and another with the points 
        #in the present. This will allow for better predictions in the neural network analysis. 
        self.lookback_points=1 ; self.data=[] ; self.data_x_1=[]
        for i in range(self.lookback_points,len(self.train_data)):
            self.data.append(self.train_data[i-self.lookback_points:i])
            self.data_x_1.append(self.train_data[i])
        
        self.data=np.array(self.data) ; self.data_x_1=np.array(self.data_x_1)

        self.data=self.data.reshape(self.data.shape[0],self.data.shape[1],1)

    def model(self):
        #Use a LSTM model twice and then move on to a relu and get one linear output
        tf.random.set_seed(42)
        self.model=Sequential()
        self.model.add(LSTM(units=128,input_shape=(self.data.shape[1],1),return_sequences=True))
        self.model.add(Dense(4,"relu"))
        self.model.add(Dense(2,"linear"))
        self.model.add(Dense(1,"linear"))

    def model_compile(self):
        self.model.compile(loss="mse",optimizer=Adam(learning_rate=0.001),metrics=['acc'])
        self.model.fit(x=self.data,y=self.data_x_1,epochs=10,shuffle=True,batch_size=1,verbose=2)

    def model_predict(self):
        self.model_prediction=self.model.predict(self.df_weekly_ridership["Value"][-201:])
        self.df_weekly_ridership["Value"]=self.df_weekly_ridership["Value"]+self.model_prediction.flatten()
        self.model_prediction=self.model.predict(self.df_weekly_ridership["Value"])

        self.model_prediction=pd.DataFrame(data={"Month And Year":self.df_weekly_ridership["Month And Year"],"Prediction":self.model_prediction.flatten()})

    def model_inverse_transform_scale(self):
        self.df_weekly_ridership["Value"]=self.scaler.inverse_transform(self.df_weekly_ridership[["Value"]])
        self.model_prediction["Prediction"]=self.scaler.inverse_transform(self.model_prediction[["Prediction"]])
        return self.df_weekly_ridership["Month And Year"],self.df_weekly_ridership["Value"], self.model_prediction["Prediction"]

    def model_plot(self):
        fig,ax=plt.subplots(1,figsize=(10,4))
        plt.plot(self.df_weekly_ridership["Month And Year"],self.df_weekly_ridership["Value"])
        plt.plot(self.model_prediction["Month And Year"],self.model_prediction["Prediction"])
        plt.setp(ax.get_xticklabels(),rotation=100)
        plt.show()

neuralnetworkanalysis=NeuralNetworkAnalysis()
neuralnetworkanalysis.create_timeline()
neuralnetworkanalysis.transform_scale_numbers()
neuralnetworkanalysis.train_data()
neuralnetworkanalysis.data_into_array()
neuralnetworkanalysis.model()
neuralnetworkanalysis.model_compile()
neuralnetworkanalysis.model_predict()
neuralnetworkanalysis.model_inverse_transform_scale()

