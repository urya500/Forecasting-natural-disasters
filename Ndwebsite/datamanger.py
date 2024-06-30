import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

file_path = 'database.csv'
df = pd.read_csv(file_path)
def statics(c,year):
    dataForC = df[(df['Country'] == f'{c}') & (df['Year'] >= year)]

    x = dataForC['Year'].values.reshape(-1, 1)
    disasters_per_year = dataForC['Year'].value_counts().sort_index()
    y = disasters_per_year.values

    unique_years = disasters_per_year.index

    plt.figure(figsize=(10, 5))
    plt.bar(disasters_per_year.index, disasters_per_year.values, color='blue')
    plt.xlabel('Year')
    plt.ylabel('Number of Natural disasters')
    plt.title(f'Number of Natural disasters in {c} per Year ({year} and later)')
    plt.xticks(rotation=45)
    plt.show()

    regressor = LinearRegression()
    regressor.fit(unique_years.values.reshape(-1, 1), y)

    y_pred = regressor.predict(unique_years.values.reshape(-1, 1))

    plt.figure(figsize=(10, 5))
    plt.scatter(unique_years, y, color='blue')
    plt.plot(unique_years, y_pred, color='red', linewidth=2)
    plt.xlabel('Year')
    plt.ylabel('Number of Natural disasters')
    plt.title(f'Linear Regression of Natural disasters in {c} ({year} and later)')
    plt.show()
