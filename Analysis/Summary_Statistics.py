import pandas as pd
import numpy as np

class SummaryStatistics:
    def __init__(self):
        self.df=pd.read_excel(r"Data\Ridership_Data.xlsx",sheet_name=None)
        pd.set_option("display.max_columns",None)
        self.daily_ridership_2022=self.df["2022 Daily Ridership"]
        self.daily_ridership_2021=self.df["2021 Daily Ridership"]
        self.daily_ridership_2020=self.df["2020 Daily Ridership"]
        self.daily_ridership_2019=self.df["2019 Daily Ridership"]
        self.monthly_ridership=self.df["Weekly TTC Ridership Data"]

    def busiest_station_2022(self):
        self.daily_ridership_2022_route_customers=self.daily_ridership_2022[["Route","Customers\nper day"]]
        self.max_2022_ridership=self.daily_ridership_2022_route_customers.loc[self.daily_ridership_2022_route_customers["Customers\nper day"].idxmax()]

        return self.max_2022_ridership[0],self.max_2022_ridership[1]

    def quietest_station_2022(self):
        self.daily_ridership_2022_route_customers=self.daily_ridership_2022[["Route","Customers\nper day"]]
        self.min_2022_ridership=self.daily_ridership_2022_route_customers.loc[self.daily_ridership_2022_route_customers["Customers\nper day"].idxmin()]

        return self.min_2022_ridership[0],self.min_2022_ridership[1]

    def busiest_month(self):
         self.busiest_month_ridership=self.monthly_ridership.loc[self.monthly_ridership["Value"].idxmax()]

         return self.busiest_month_ridership[0],self.busiest_month_ridership[1],self.busiest_month_ridership[2]
        

    def quietest_month(self):
        self.quietest_month_ridership=self.monthly_ridership.loc[self.monthly_ridership["Value"].idxmin()]

        return self.quietest_month_ridership[0],self.quietest_month_ridership[1],self.quietest_month_ridership[2]

    def busiest_station_per_year(self):
        self.daily_ridership_2021_route_customers=self.daily_ridership_2021[["Route","Customers\nper day"]]
        self.max_2021_ridership=self.daily_ridership_2021_route_customers.loc[self.daily_ridership_2021_route_customers["Customers\nper day"].idxmax()]
        
        self.daily_ridership_2020_route_customers=self.daily_ridership_2020[["Route","Customers per day"]]
        self.max_2020_ridership=self.daily_ridership_2020_route_customers.loc[self.daily_ridership_2020_route_customers["Customers per day"].idxmax()]
 
        self.daily_ridership_2019_route_customers=self.daily_ridership_2019[["Route","Customers per day"]]
        self.max_2019_ridership=self.daily_ridership_2019_route_customers.loc[self.daily_ridership_2019_route_customers["Customers per day"].idxmax()]        

        return self.max_2021_ridership[0],self.max_2021_ridership[1],self.max_2020_ridership[0],self.max_2020_ridership[1],self.max_2019_ridership[0],self.max_2019_ridership[1]


summarystatistics=SummaryStatistics()
summarystatistics.busiest_station_2022()
summarystatistics.quietest_station_2022()
summarystatistics.busiest_month()
summarystatistics.quietest_month()
summarystatistics.busiest_station_per_year()