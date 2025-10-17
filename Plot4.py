#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importing the data. Once again, we have to take every 5 years

import pandas as pd
df = pd.read_csv("data/healthcare_data.csv")
specific_countries = ["Canada","USA"]
specific_years = [1990, 1995, 2000, 2005, 2010, 2015, 2020]

canada_data = df[(df["Year"].isin(specific_years)) & (df["Country"].isin(["Canada"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])
    
us_data = df[(df["Year"].isin(specific_years)) & (df["Country"].isin(["USA"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])


# Plotting the data - bar plot

import matplotlib.pyplot as plt
import numpy as np

# Subplot 1 - Canada
plt.subplot(1, 2, 1)
x = np.array(["'90", "'95", "'00", "'05", "'10", "'15", "'20"])
y = canada_data.Infant_Mortality_per_1000
plt.title("Canada")
plt.xlabel("Year")
plt.ylabel("Infant Mortality per 1000 Babies")
plt.bar(x,y)

# Subplot 2 - USA
plt.subplot(1, 2, 2)
x = np.array(["'90", "'95", "'00", "'05", "'10", "'15", "'20"])
y = us_data.Infant_Mortality_per_1000
plt.title("USA")
plt.xlabel("Year")
plt.bar(x,y)

plt.suptitle("Infant Mortality Rate per 5 Years in Canada and the USA from 1990 to 2020")
plt.show()

# Explanation: The chart shows fluctuations in infant mortality rates over the years. There is no evident visual trend here, however, the US has the lowest recorded value on the whole graph in 2010, and in the most recent year, 2020, the USA has a lower infant mortality than Canada. 