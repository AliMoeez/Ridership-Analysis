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

         return self.busiest_month_ridership[0],self.busiest_month_ridership[1],self.busiest_month_ridership[2],self.busiest_month_ridership[3]
        

    def quietest_month(self):
        self.quietest_month_ridership=self.monthly_ridership.loc[self.monthly_ridership["Value"].idxmin()]

        return self.quietest_month_ridership[0],self.quietest_month_ridership[1],self.quietest_month_ridership[2],self.quietest_month_ridership[3]

    def busiest_station_per_year(self):
        self.daily_ridership_2021_route_customers=self.daily_ridership_2021[["Route","Customers\nper day"]]
        self.max_2021_ridership=self.daily_ridership_2021_route_customers.loc[self.daily_ridership_2021_route_customers["Customers\nper day"].idxmax()]
        
        self.daily_ridership_2020_route_customers=self.daily_ridership_2020[["Route","Customers per day"]]
        self.max_2020_ridership=self.daily_ridership_2020_route_customers.loc[self.daily_ridership_2020_route_customers["Customers per day"].idxmax()]
 
        self.daily_ridership_2019_route_customers=self.daily_ridership_2019[["Route","Customers per day"]]
        self.max_2019_ridership=self.daily_ridership_2019_route_customers.loc[self.daily_ridership_2019_route_customers["Customers per day"].idxmax()]        

        return self.max_2021_ridership[0],self.max_2021_ridership[1],self.max_2020_ridership[0],self.max_2020_ridership[1],self.max_2019_ridership[0],self.max_2019_ridership[1]
    
    def monthly_ridership_percent_change(self):
        self.monthly_ridership_change=self.monthly_ridership["Value"].pct_change()
        self.monthly_ridership_change=self.monthly_ridership_change*100

        return self.monthly_ridership_change

    def am_vehicle_peak(self):
        self.df_am_vechicle_peak=pd.DataFrame(
            data={
                "Year":["2022","2021","2020","2019"],
                "Value": [np.average(self.daily_ridership_2022["Vehicles in\nAM peak"]), np.average(self.daily_ridership_2021["Vehicles in a.m.\npeak"]), 
                          np.average(self.daily_ridership_2020["Vehicles in a.m. peak"].dropna()), np.average(self.daily_ridership_2019["Vehicles in a.m. peak"].dropna())]

            }
        )

        return self.df_am_vechicle_peak
    
    def pm_vehicle_peak(self):
        self.df_pm_vechicle_peak=pd.DataFrame(
            data={
                "Year":["2022","2021","2020","2019"],
                "Value": [np.average(self.daily_ridership_2022["Vehicles in\nPM peak"]),np.average(self.daily_ridership_2021["Vehicles in p.m.\npeak"]), 
                        np.average(self.daily_ridership_2020["Vehicles in p.m. peak"].dropna()),np.average(self.daily_ridership_2019["Vehicles inp.m. peak"].dropna())]
            }
        )


        return self.df_pm_vechicle_peak
    
    def both_vechicle_peak(self):
        self.df_both_vechicle_peak=pd.DataFrame(
            data={

                "2022": self.daily_ridership_2022["Vehicles in\nPM peak"],
                "2021": self.daily_ridership_2021["Vehicles in p.m.\npeak"],
                "2020": self.daily_ridership_2020["Vehicles in p.m. peak"],
                "2019": self.daily_ridership_2019["Vehicles inp.m. peak"],
                
                "2022": self.daily_ridership_2022["Vehicles in\nAM peak"],
                "2021": self.daily_ridership_2021["Vehicles in a.m.\npeak"],
                "2020": self.daily_ridership_2020["Vehicles in a.m. peak"],
                "2019": self.daily_ridership_2019["Vehicles in a.m. peak"],
            }
        )


        return self.df_both_vechicle_peak

    
    def top_ten_stations_2022(self):
        self.station_and_value_2022=self.daily_ridership_2022[["Route","Customers\nper day"]]
        self.station_and_value_2022=self.station_and_value_2022.sort_values("Customers\nper day",ascending=False)
        self.station_and_value_2022=self.station_and_value_2022.nlargest(10,"Customers\nper day")

        self.station_and_value_2021=self.daily_ridership_2021[["Route","Customers\nper day"]]
        self.station_and_value_2021=self.station_and_value_2021.sort_values("Customers\nper day",ascending=False)
        self.station_and_value_2021=self.station_and_value_2021.nlargest(10,"Customers\nper day")

        self.station_and_value_2020=self.daily_ridership_2020[["Route","Customers per day"]]
        self.station_and_value_2020=self.station_and_value_2020.sort_values("Customers per day",ascending=False)
        self.station_and_value_2020=self.station_and_value_2020.nlargest(10,"Customers per day")

        self.station_and_value_2019=self.daily_ridership_2019[["Route","Customers per day"]]
        self.station_and_value_2019=self.station_and_value_2019.sort_values("Customers per day",ascending=False)
        self.station_and_value_2019=self.station_and_value_2019.nlargest(10,"Customers per day")
        
        return self.station_and_value_2022,self.station_and_value_2021,self.station_and_value_2020,self.station_and_value_2019
            
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
    
    def dataframe_monthly_percent_change(self):
        self.monthly_ridership_year_string=self.monthly_ridership["Year"].astype(str)


        self.df_monthly_percent_change=pd.DataFrame(
            data={
                "Period": self.monthly_ridership["Period"] + " " + self.monthly_ridership_year_string,
                "Values" : SummaryStatistics.monthly_ridership_percent_change(self)
            }
        )

        return self.df_monthly_percent_change

summarystatistics=SummaryStatistics()
summarystatistics.busiest_station_2022()
summarystatistics.quietest_station_2022()
summarystatistics.busiest_month()
summarystatistics.quietest_month()
summarystatistics.busiest_station_per_year()
summarystatistics.monthly_ridership_percent_change()
summarystatistics.am_vehicle_peak()
summarystatistics.pm_vehicle_peak()
summarystatistics.both_vechicle_peak()
summarystatistics.top_ten_stations_2022()
summarystatistics.dataframe_max_stations()
summarystatistics.dataframe_monthly_percent_change()