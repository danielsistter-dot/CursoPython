import streamlit as st
import pandas as pd

caminho_compras = "Projeto_Pandas/Dados/compras.csv"
df_compras = pd.read_csv(caminho_compras,sep=";",decimal=",")


st.dataframe(df_compras)