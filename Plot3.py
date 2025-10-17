#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
df = pd.read_csv("data/healthcare_data.csv")
specific_countries = ["Canada","USA"]

# We don't want data every 5 years, instead, we want a scatter of all the data, so we remove the specific_years

canada_data = df[(df["Country"].isin(["Canada"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])
    
us_data = df[(df["Country"].isin(["USA"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])


# Plotting two graphs side by side

import matplotlib.pyplot as plt


# Plot 1 - Canada
plt.subplot(1, 2, 1)
plt.scatter(canada_data.Healthcare_Spending_GDP_percent,canada_data.Life_Expectancy, color="blue")
plt.title("Canada")
plt.xlabel("Healthcare Spending (% of GDP)")
plt.ylabel("Life Expectancy (years)")
plt.grid(True)

# Plot 2 - USA
plt.subplot(1, 2, 2)
plt.scatter(us_data.Healthcare_Spending_GDP_percent, us_data.Life_Expectancy, color="orange")
plt.title("USA")
plt.xlabel("Healthcare Spending (% of GDP)")
plt.grid(True)

plt.suptitle("Healthcare Spending vs Life Expectancy (Canada vs USA, 1990–2020)")
plt.show()