import pandas as pd
import numpy as np 
import geopy.distance


class Map:
    def __init__(self):
        self.df=pd.read_excel(r"Data\Ridership_Data.xlsx",sheet_name=None)
        self.map_data=self.df['Address Book For Stations']
        
        self.map_data.loc[self.map_data["Station Name"]=="St. George","Latitude"]=43.6682
        self.map_data.loc[self.map_data["Station Name"]=="St. George","Longitude"]=-79.40009
        
        self.map_data.loc[self.map_data["Station Name"]=="Queen's Park","Latitude"]=43.65967
        self.map_data.loc[self.map_data["Station Name"]=="Queen's Park","Longitude"]=-79.39078
        pd.set_option("display.max_columns",None)

    def data(self):
        return self.map_data
    
    def max_min_stations(self):
        self.max_ridership=self.map_data.loc[self.map_data["Ridership (2014 Daily Average)"]==self.map_data["Ridership (2014 Daily Average)"].max(),"Station Name"].values[0]
        self.min_ridership=self.map_data.loc[self.map_data["Ridership (2014 Daily Average)"]==self.map_data["Ridership (2014 Daily Average)"].min(),"Station Name"].values[0]

    def distance(self):
        self.map_distance_list=[]
        for i in range(1,self.map_data.shape[0]):
            self.map_distance_list.append(
                geopy.distance.geodesic(
                    (self.map_data["Latitude"][0],self.map_data["Longitude"][0]),(self.map_data["Latitude"][i],self.map_data["Longitude"][i])          
                ).km
            )
        self.average_distance=np.average(self.map_distance_list)
    
    def map_other_data(self):

        self.df=pd.DataFrame(
            data={
                "Number of Stations": [self.map_data.shape[0]],
                "Most Riders" : [self.max_ridership],
                "Least Riders":[self.min_ridership],
                "Average Distance Between Stations" : [self.average_distance],
            }
        )

        print(self.df["Average Distance Between Stations"][0])

        return self.df


map=Map()
map.data()
map.max_min_stations()
map.distance()
map.map_other_data()