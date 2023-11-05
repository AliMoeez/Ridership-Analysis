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

    def train_test_data(self):
        #Split The Data into one training set and one testing set
        #Training set gets 100 data points and Test sett gets the remainder 100 data points
        self.train_data=self.df_weekly_ridership["Value"][:100] ; self.test_data=self.df_weekly_ridership["Value"][100:]

    def data_into_array(self):
        #Create datsasets where one dataset looks 10 points in the points, and another with the points 
        #in the present. This will allow for better predictions in the neural network analysis. 
        self.lookback_points=10 ; self.data=[] ; self.data_x_1=[]
        for i in range(self.lookback_points,len(self.train_data)):
            self.data.append(self.train_data[i-self.lookback_points:i])
            self.data_x_1.append(self.train_data[i])
        
        self.data=np.array(self.data) ; self.data_x_1=np.array(self.data_x_1)

        self.data=self.data.reshape(self.data.shape[0],self.data.shape[1],1)

    def model(self):
        #Use a LSTM model twice and then move on to a relu and get one linear output
        self.model=Sequential()
        self.model.add(LSTM(units=64,input_shape=(self.data.shape[1],1),return_sequences=True))
        self.model.add(LSTM(units=32))
        self.model.add(Dense(16,"relu"))
        self.model.add(Dense(1,"linear"))

    def model_compile(self):
        pass

    def model_predict(self):
        pass

    def model_inverse_transform_scale(self):
        pass

    def model_plot(self):
        pass

neuralnetworkanalysis=NeuralNetworkAnalysis()
neuralnetworkanalysis.create_timeline()
neuralnetworkanalysis.transform_scale_numbers()
neuralnetworkanalysis.train_test_data()
neuralnetworkanalysis.data_into_array()
neuralnetworkanalysis.model()
neuralnetworkanalysis.model_compile()
neuralnetworkanalysis.model_inverse_transform_scale()
neuralnetworkanalysis.model_predict()

