import streamlit as st
import pandas as pd

df = pd.read_csv('analise_dados/coffee_data.csv')

st.title("Dashboard - Vendas de Café")

product = st.selectbox("Selecione o produto", df['product'].unique())

filtered_data = df[df[df['product'] == product]]

st.write(filtered_data)

st.bar_chart(filtered_data.groupby('date')['money'].sum())

