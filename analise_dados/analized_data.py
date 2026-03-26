import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('coffee_data.csv')
print(df.head(5))

df = df.dropna()

month_sales = df.groupby(["date"])["money"].sum()

month_sales.plot(kind='bar')
plt.title('Total Sales by Month')
plt.show() 

