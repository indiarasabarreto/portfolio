import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('coffee_data.csv')

df = df.dropna()

month_sales = df.groupby('Month')['Sales'].sum()

month_sales.plot(kind='bar')
plt.title('Total Sales by Month')
plt.show()