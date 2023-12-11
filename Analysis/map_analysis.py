import pandas as pd


class Map:
    def __init__(self):
        self.df=pd.read_excel(r"Data\Ridership_Data.xlsx",sheet_name=None)
        self.map_data=self.df['Address Book For Stations']
        self.map_data.loc[self.map_data["Station Name"]=="Queen's Park","Latitude"]=43.65967
        self.map_data.loc[self.map_data["Station Name"]=="Queen's Park","Longitude"]=-79.39078
        pd.set_option("display.max_columns",None)

    def data(self):
        return self.map_data


map=Map()
map.data()