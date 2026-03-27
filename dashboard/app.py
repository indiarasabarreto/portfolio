import streamlit as st
import pandas as pd

df = pd.read_csv('coffee_data.csv')

st.title("Dashboard de Vendas")

product = st.selectbox("Escolha o produto", df['coffee_name'].unique())

filtered_data = df[df[df['product'] == product]]

st.write(filtered_data)

st.bar_chart(filtered_data.groupby('date')['money'].sum())

