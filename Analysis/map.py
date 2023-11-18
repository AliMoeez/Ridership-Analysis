import pandas as pd


class Map:
    def __init__(self):
        self.df=pd.read_excel(r"Data\Ridership_Data.xlsx",sheet_name=None)
        self.map_data=self.df['Address Book For Stations']
        pd.set_option("display.max_columns",None)

    def storage(self):
        self.map_station=self.map_data["Station Name"]
        self.map_ridership=self.map_data["Ridership (2014 Daily Average)"]
        self.map_address=self.map_data["Address"]
        self.map_latitutde=self.map_data["Latitude"]
        self.map_longitude=self.map_data["Longitude"]
        return self.map_station,self.map_ridership,self.map_address,self.map_latitutde,self.map_longitude

map=Map()
map.storage()