
import pandas as pd

df = pd.read_csv("C:/Users/6304301/Downloads/New folder/healthcare_access_countries.csv")

import matplotlib.pyplot as plt

specific_countries = ["Canada","USA"]

canada_data = df[(df["Country"].isin(["Canada"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])
    
us_data = df[(df["Country"].isin(["USA"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])



# Plotting the data

plt.pie([canada_data.Doctors_per_1000.mean(), us_data.Doctors_per_1000.mean()], labels = ["Canada", "USA"], autopct = '%1.1f%%', startangle = 90)
plt.title("Average Doctors per 1000 People (1990-2020)")
plt.show()

# Explanation: The plot compares the average number of doctors per 1000 people in Canada and the USA from 1990 to 2020. Each portion of the chart represents the share of doctors per population for that country. Canada holds a slightly larger proportion, with 51.1% compared to the United States at 48.9%. This indictates that, on average, maintains a higher availability of medical professionals relative to its population across the studied period.