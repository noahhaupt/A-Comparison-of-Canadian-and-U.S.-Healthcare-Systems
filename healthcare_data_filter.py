# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv("data/healthcare_data.csv")


# Filtering the data:
    

# This converts to data to a list of lists
rows = data.values.tolist()

filtered_rows = []

for row in rows:
    country = row[1]     # The second column is country
    
# Keeps only Canada and USA
    if country == "Canada" or country == "USA":
       # Skips hospital beds since it is the 4th column (4th item in first row) in the data
        new_row = [row[0], row[1], row[2], row[4], row[5], row[6]]
        filtered_rows.append(new_row)

print("Filtered Data (Canada & USA, no Hospital Beds):", filtered_rows)


#The data was filtered to only contain values from Canada and USA, and not Nigeria, India, and Germany, since we are only concerned with comparing those two countries. The data was also filtered to remove the  hospital beds per 100 column, since we did not ask for this in our research proposal questions. 