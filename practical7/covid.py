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

