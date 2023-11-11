import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


class TTest:
    def __init__(self):
        #Lode the dataset from the ridership data excel file and find the appropirate sheet
        self.df=pd.read_excel(r"Data\Ridership_Data.xlsx",sheet_name=None)
        self.daily_ridership_data=self.df["2022 Daily Ridership"]
        pd.set_option('display.max_columns',None)
        self.customers_per_day=self.daily_ridership_data["Customers\nper day"]
        self.hours_per_weekday=self.daily_ridership_data["Hours per\nWeekday"]
        self.kilometres_per_day=self.daily_ridership_data["Kilometres per\nWeekday"]
        self.average_daily_buses=(self.daily_ridership_data["Vehicles in\nAM peak"]+self.daily_ridership_data["Vehicles in\nPM peak"])/2    

    def customer_day_vs_hours_per_day(self):
        #Do a independent t-test for customers per day and hours per weekday. This will help find if their
        #if customers per day effects the hours per weekday of buses
        self.ttest_one=ttest_ind(self.customers_per_day,self.hours_per_weekday)
        self.ttest_one_test_statistic=self.ttest_one[0]
        self.ttest_one_p_value=self.ttest_one[1]
        #Find t-statistic is 11.55 and the p-value is <0.05 meaning that customers 
        #per day does indeed have a effect on the hourrs per weekday of buses

    def customer_day_vs_km_per_day(self):
        #Do a independent t-test for customers per day and km per weekday. This will help find if their
        #if customers per day effects the km per weekday of buses
        self.ttest_two=ttest_ind(self.customers_per_day,self.kilometres_per_day)
        self.ttest_two_test_statistic=self.ttest_two[0]
        self.ttest_two_p_value=self.ttest_two[1]
        #Find t-statistic is 7.69 and the p-value is <0.05 meaning that customers 
        #per day does indeed have a effect on the km per weekday of buses

    def customer_day_vs_average_daily_vehicles(self):
        #Do a independent t-test for customers per day and average buses per weekday. This will help find if their
        #if customers per day effects the average buses per weekday.
        self.ttest_three=ttest_ind(self.customers_per_day,self.average_daily_buses)
        self.ttest_three_test_statistic=self.ttest_three[0]
        self.ttest_three_p_value=self.ttest_three[1]
        #Find t-statistic is 11.76 and the p-value is <0.05 meaning that customers 
        #per day does indeed have a effect on the average buses per weekday.

    def graphs(self):
        pass


ttest=TTest()
ttest.customer_day_vs_hours_per_day()
ttest.customer_day_vs_km_per_day()
ttest.customer_day_vs_average_daily_vehicles()
ttest.graphs()