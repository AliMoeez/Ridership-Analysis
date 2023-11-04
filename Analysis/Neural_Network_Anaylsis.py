import pandas as pd 



class NeuralNetworkAnalysis:
    def __init__(self) -> None:
        self.df=pd.read_excel(r"Data\Ridership_Data.xlsx",sheet_name=None)
        self.df_weekly_ridership=self.df["Weekly TTC Ridership Data"]
        self.df_weekly_ridership["Month And Year"]=self.df_weekly_ridership["Period"]+ " " +self.df_weekly_ridership["Year"].astype(str)
        print(self.df_weekly_ridership)

    def create_timeline(self):
        pass

    def transform_scale_numbers(self):
        pass

    def train_test_data(self):
        pass

    def data_into_array(self):
        pass

    def model(self):
        pass

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

