#import pandas
#Change the working directory to the location of the file (practical7)
#use the pandas library to read the content of the .csv file into a dataframe object called covid_data
#use iloc to show the second column from every 100th row from the first 1000 rows
#Filter all new cases and deaths in the data up to 2020-03-31 and name it new_data
#Output the mean, quartiles, etc. of the data in new_data to describe the data
#Filter the mean value in new_data.describe() and name it proportion1
#Calculate the percentage
#Filtering new_case data in new_data and plotting box plots
#Filtering new_deaths data in new_data and plotting box plots
#To obtain a global graph of new cases over time, first add up the number of new cases in different locations on the same day
#Define world_dates as the date left after the summation (x-axis)
#Define world_new_cases to be the summed number of new cases worldwide
#The same steps are repeated to plot a line graph of new deaths over time
#Next, answer the questions in question.txt by filtering the data for locations in Austria and retaining their dates and total_cases
#Name austria_time and austria_total_cases as the date (x-axis) and the total number of cases (y-axis) 
#Final plot

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/jishuhan/Downloads/IBI1_2022-23/practical7")#Convert the current directory to practical7
covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[0:1001:100,1])
print(covid_data.loc[covid_data["location"]=="Afghanistan","total_cases"])
my_columns = [False, True, True, True, False, False]
new_data=covid_data.loc[covid_data["date"]=="2020-03-31",my_columns]
print(new_data.describe())
proportion=new_data.describe()
my_colomn=[True,True]
#The code comes from the Internet
proportion1=proportion.loc['mean',my_colomn]
proportion1['percent1']=proportion1['new_deaths']/proportion1['new_cases']
print(proportion1)
my_columns=[False,True,False]
world_dates2=new_data.iloc[:,my_columns]
world_dates2.plot.box()
plt.show()
my_columns=[False,False,True]
world_dates1=new_data.iloc[:,my_columns]
world_dates1.plot.box()
plt.show()
my_columns=[True,False,True,False,False,False]
df=covid_data.iloc[:,my_columns]
df.groupby=df.groupby("date", as_index=False).sum(numeric_only=True)
world_new_cases=df.groupby.iloc[:,1]
world_dates=df.groupby.iloc[:,0]
plt.plot(world_dates, world_new_cases, 'bo')
plt.show()
my_columns=[True,False,False,True,False,False]
df=covid_data.iloc[:,my_columns]
df.groupby=df.groupby("date", as_index=False).sum(numeric_only=True)
world_new_deaths=df.groupby.iloc[:,1]
world_dates=df.groupby.iloc[:,0]
plt.plot(world_dates, world_new_deaths, 'bo')
plt.show()

my_colomn=[True,False,False,False,True,False]
Austria_data=covid_data.loc[covid_data["location"]=="Austria",my_colomn]
Austria_time=Austria_data.iloc[:,0]
Austria_total_cases=Austria_data.iloc[:,1]
plt.plot(Austria_time, Austria_total_cases, 'bo')
plt.show()
