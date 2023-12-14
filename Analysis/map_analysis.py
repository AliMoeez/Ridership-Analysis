import pandas as pd
import numpy as np 


class Map:
    def __init__(self):
        self.df=pd.read_excel(r"Data\Ridership_Data.xlsx",sheet_name=None)
        self.map_data=self.df['Address Book For Stations']
        self.map_data.loc[self.map_data["Station Name"]=="Queen's Park","Latitude"]=43.65967
        self.map_data.loc[self.map_data["Station Name"]=="Queen's Park","Longitude"]=-79.39078
        pd.set_option("display.max_columns",None)

        print(self.map_data)

        self.max_ridership=np.max(self.map_data["Ridership (2014 Daily Average)"])

        print(self.max_ridership)

    def data(self):
        return self.map_data
    
    def map_df(self):

        self.df=pd.DataFrame(
            data={
                "Number of Stations": [self.map_data.shape[0]]
            }
        )

        print(self.df)


map=Map()
map.data()
map.map_df()