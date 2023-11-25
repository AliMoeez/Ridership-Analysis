import pandas as pd
import numpy as np

class SummaryStatistics:
    def __init__(self):
        self.df=pd.read_excel(r"Data\Ridership_Data.xlsx",sheet_name=None)
        pd.set_option("display.max_columns",None)
        pd.set_option("mode.chained_assignment",None)
        self.daily_ridership_2022=self.df["2022 Daily Ridership"]
        self.daily_ridership_2021=self.df["2021 Daily Ridership"]
        self.daily_ridership_2020=self.df["2020 Daily Ridership"]
        self.daily_ridership_2019=self.df["2019 Daily Ridership"]
        self.monthly_ridership=self.df["Weekly TTC Ridership Data"]

    def busiest_station_2022(self):
        self.daily_ridership_2022_route_customers=self.daily_ridership_2022[["Route","Customers\nper day"]]
        self.max_2022_ridership=self.daily_ridership_2022_route_customers.loc[self.daily_ridership_2022_route_customers["Customers\nper day"].idxmax()]
        self.max_2022_ridership[0]=self.max_2022_ridership[0]+"."
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
    
    def dataframe_max_stations(self):
        self.df_max_station=pd.DataFrame(
            data={
                "Year":["2022","2021","2020","2019"],
                
                "Station":[SummaryStatistics.busiest_station_2022(self)[0],SummaryStatistics.busiest_station_per_year(self)[0],
                            SummaryStatistics.busiest_station_per_year(self)[2],SummaryStatistics.busiest_station_per_year(self)[4]],
             
                "Value":[SummaryStatistics.busiest_station_2022(self)[1],SummaryStatistics.busiest_station_per_year(self)[1],
                         SummaryStatistics.busiest_station_per_year(self)[3],SummaryStatistics.busiest_station_per_year(self)[5]],
            }
        )


        return self.df_max_station

summarystatistics=SummaryStatistics()
summarystatistics.busiest_station_2022()
summarystatistics.quietest_station_2022()
summarystatistics.busiest_month()
summarystatistics.quietest_month()
summarystatistics.busiest_station_per_year()

summarystatistics.dataframe_max_stations()


      #     "Year":["2022","2021","2020","2019"],
      #          
      #          "Station":[SummaryStatistics.busiest_station_2022(self)[0],SummaryStatistics.busiest_station_per_year(self)[0],
      #                      SummaryStatistics.busiest_station_per_year(self)[2],SummaryStatistics.busiest_station_per_year(self)[4]],
      #          
      ##          "Value":[SummaryStatistics.busiest_station_2022(self)[1],SummaryStatistics.busiest_station_per_year(self)[1],
       #                     SummaryStatistics.busiest_station_per_year(self)[3],SummaryStatistics.busiest_station_per_year(self)[5]],


       #            "2022":[SummaryStatistics.busiest_station_2022(self)[1]],
       #         "2021":[SummaryStatistics.busiest_station_per_year(self)[1]],
       #         "2020":[SummaryStatistics.busiest_station_per_year(self)[3]],
       #         "2019":[SummaryStatistics.busiest_station_per_year(self)[5]]