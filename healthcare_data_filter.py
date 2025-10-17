# -*- coding: utf-8 -*-

import pandas as pd


# Import the data fom computer using pandas function

df = pd.read_csv("data/healthcare_access_countries.csv")


# Create a new variable containing only the needed countries for this lab (Canada and USA)

specific_countries = ["Canada","USA"]


# Filtered data should now only contain countries in the specific_countries variable.
# Filtered data will include 6 of the 7 columns of the data (since we are not looking for information on hospital beds per 1000)

filtered_data = df[df["Country"].isin(specific_countries)].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])


print(filtered_data)

# The filtered data prints 62 rows (Canada and USA only) and the 6 required columns


# Summary: The data was filtered to only contain values from Canada and USA, and not Nigeria, India, and Germany, since we are only concerned with comparing those two countries. The data was also filtered to remove the  hospital beds per 100 column, since we did not ask for this in our research proposal questions. 