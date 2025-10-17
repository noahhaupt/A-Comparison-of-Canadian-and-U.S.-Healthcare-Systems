#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
df = pd.read_csv("data/healthcare_data.csv")
specific_countries = ["Canada","USA"]
specific_years = [1990, 1995, 2000, 2005, 2010, 2015, 2020]

canada_data = df[(df["Year"].isin(specific_years)) & (df["Country"].isin(["Canada"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])
    
us_data = df[(df["Year"].isin(specific_years)) & (df["Country"].isin(["USA"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])


# Plotting the data

import matplotlib.pyplot as plt

plt.plot(canada_data.Year,canada_data.Healthcare_Spending_GDP_percent, label = "Canada", marker = "o")
plt.plot(us_data.Year,us_data.Healthcare_Spending_GDP_percent, label = "USA", marker = "o")
plt.title("Comparing Healthcare Spending in Canada and USA Every 5 Years from 1990 to 2020")
plt.xlabel("Year")
plt.ylabel("Healthcare Spending (% of GDP)")
plt.legend()
plt.grid(True)
plt.show()

# Explanation: 