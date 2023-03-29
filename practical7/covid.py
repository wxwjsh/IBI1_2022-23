#import pandas
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
