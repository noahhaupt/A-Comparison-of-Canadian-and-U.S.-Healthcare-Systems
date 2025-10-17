import pandas as pd

df = pd.read_csv("C:/Users/6304301/Downloads/New folder/healthcare_access_countries.csv")

import matplotlib.pyplot as plt

#HISTOGRAM
#This plot shows how Life Expectancy values are distributed in the dataset.

specific_countries = ["Canada","USA"]

canada_data = df[(df["Country"].isin(["Canada"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])
    
us_data = df[(df["Country"].isin(["USA"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])


# Plotting two graphs side by side

# Plot 1 - Canada
plt.subplot(1, 2, 1)
plt.hist(canada_data.Life_Expectancy,color = "blue", edgecolor = "black")
plt.title("Canada")
plt.xlabel("Life Expectancy (years)")
plt.ylabel("Distribution")
plt.grid(True)


# Plot 2 - USA
plt.subplot(1, 2, 2)
plt.hist(us_data.Life_Expectancy, color = "orange", edgecolor = "black")
plt.title("USA")
plt.xlabel("Life Expectancy (years)")
plt.grid(True)

plt.suptitle("Distribution of Life Expectancy of Canada vs. USA from 1990-2020")
plt.show()

# Explanation: The graph displays how life expectancy values are distributed for Canada and the Unites States between 1990 and 2020. Each bar represents the frequency of life expectancy within a specific range for that country. Throughout most of the time period, Canada's distribution is slightly shifted toward higher values, indicating longer average lifespans. The USA suggests greater variation and slightly lower overall life expectancy levels compared to Canada.