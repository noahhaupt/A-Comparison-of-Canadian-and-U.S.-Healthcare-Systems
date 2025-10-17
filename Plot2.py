#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
df = pd.read_csv("data/healthcare_access_countries.csv")
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

# Explanation: The graph compares healthcare spending in Canada (blue) and the USA (orange) every 5 years from 1990 to 2020. Both countries show a very similar trend over the 30 years, with USA spending slightly more from 2000 to 2015, to 2020, where the GDP spending percent is almost the same. This helps us a lot with our research, showing that the two countries spend similar amounts, making it easier to understand their efficiency when we look at other graphs.