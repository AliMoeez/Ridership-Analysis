import pandas as pd


class Map:
    def __init__(self):
        self.df=pd.read_excel(r"Data\Ridership_Data.xlsx",sheet_name=None)
        self.map_data=self.df['Address Book For Stations']
        pd.set_option("display.max_columns",None)

    def data(self):
        return self.map_data


map=Map()
map.data()