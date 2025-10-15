#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv("data/healthcare_data.csv")

import matplotlib.pyplot as plt

canada = data[data["Country"] == "Canada"].sort_values("Year")
usa = data[data["Country"] == "USA"].sort_values("Year")

plt.plot(canada["Year"], canada["Life_Expectancy"], label="Canada", linestyle="solid")
plt.plot(usa["Year"], usa["Life_Expectancy"], label="USA", linestyle="dashed")

plt.title("Life Expectancy in Canada and USA (1990–2020)")
plt.xlabel("Year")
plt.ylabel("Life Expectancy (years)")
plt.legend()
plt.grid()
plt.show()
