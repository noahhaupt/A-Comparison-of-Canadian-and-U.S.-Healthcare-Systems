#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Filtered data (from previous python sheet):
import pandas as pd
df = pd.read_csv("data/healthcare_data.csv")
specific_countries = ["Canada","USA"]
filtered_data = df[df["Country"].isin(specific_countries)].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])

# Life expectancy vs time between us and canada every 5 years between 1990 and 2020

# We need to filter the data even more to contain every 5 years between 1990 and 2020 in order to simplify the graph.

specific_years = [1990, 1995, 2000, 2005, 2010, 2015, 2020]

filtered_data_years = df[(df["Year"].isin(specific_years)) & (df["Country"].isin(specific_countries))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])

# Now let's split up the data into USA and Canada

canada_data = df[(df["Year"].isin(specific_years)) & (df["Country"].isin(["Canada"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])
    
us_data = df[(df["Year"].isin(specific_years)) & (df["Country"].isin(["USA"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])

# Plotting the data

import matplotlib.pyplot as plt

plt.plot(canada_data.Year,canada_data.Life_Expectancy, label = "Canada", marker = "o")
plt.plot(us_data.Year,us_data.Life_Expectancy, label = "USA", marker = "o")
plt.title("LLife Expectancy in Canada vs USA (Every 5 Years from 1990 to 2020)")
plt.xlabel("Year")
plt.ylabel("Life Expectancy (years)")
plt.legend()
plt.grid(True)
plt.show()