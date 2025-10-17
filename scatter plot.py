

import pandas as pd

df = pd.read_csv("C:/Users/6304301/Downloads/New folder/healthcare_access_countries.csv")
import matplotlib.pyplot as plt

specific_years = [1990, 2000, 2010, 2020]

specific_countries = ["Canada","USA"]

canada_data = df[(df["Year"].isin(specific_years)) & (df["Country"].isin(["Canada"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])
    
us_data = df[(df["Year"].isin(specific_years)) & (df["Country"].isin(["USA"]))].filter(items=["Year","Country","Life_Expectancy","Doctors_per_1000","Healthcare_Spending_GDP_percent","Infant_Mortality_per_1000"])



# Plotting the data


plt.plot(canada_data.Year,canada_data.Infant_Mortality_per_1000, label = "Canada", marker = "o")
plt.plot(us_data.Year,us_data.Infant_Mortality_per_1000, label = "USA", marker = "o")
plt.title("Infant mortality...")
plt.xlabel("Year")
plt.ylabel("Infant Mortality per 1000 babies")
plt.legend()
plt.grid(True)
plt.show()

# Explanation: This plot displays the changes in infant mortality rates for Canada and the Unites States for 1990 to 2020. Each point represents the number of infant deaths per 1000 live births for that year. Both countries show a clear decline in infant mortality over time, reflecting improvements in healthcare and early childhood support. However, the USA consistently remains slightly lower than Canada, highlighting its stronger reduction in infant deaths in recent years.
