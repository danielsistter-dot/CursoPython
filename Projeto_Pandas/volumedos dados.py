import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta

caminho_datasets = "Projeto_Pandas/Dados"

df_compras = pd.read_csv(f"{caminho_datasets}/compras.csv", sep=";",decimal=",",index_col=0,parse_dates=True)
df_lojas =pd.read_csv(f"{caminho_datasets}/lojas.csv", sep=";",decimal=",", index_col=0)
df_produtos =pd.read_csv(f"{caminho_datasets}/produtos.csv", sep=";",decimal=",",index_col=0)

df_produtos=df_produtos.rename(columns={"NOME":"produto"})


df_compras =df_compras.reset_index()
df_compras = pd.merge(left=df_compras,
                      right=df_produtos[["preco","produto"]],
                      on="produto",
                      how="left"
                      )
df_compras =df_compras.set_index("data")
df_compras["Comissao"]=df_compras["preco"]*0.05

data_default = df_compras.index.date.max()
data_inicio= st.sidebar.date_input("Data inicial", data_default - timedelta(days=6))
data_final = st.sidebar.date_input("Data final",data_default)

df_compras_filter = df_compras[(df_compras.index.date >=data_inicio)&(df_compras.index.date < data_final + timedelta(days=1))]

st.markdown("# Numeros Gerais")

col1, col2 =st.columns(2)

valor_compras = df_compras_filter["preco"].sum()
valor_compras = f"R$ {valor_compras:.2f}"
col1.metric("Valor de compras no periodo",valor_compras)
col2.metric("Quantidade de compras no periodo",df_compras_filter["preco"].count())

st.divider()

princial_loja = df_compras_filter["loja"].value_counts().index[0]
st.markdown(f"# Principal Loja: {princial_loja}")
col21,col22 = st.columns(2)

valor_compras_loja =df_compras_filter  [df_compras_filter["loja"]== princial_loja]["preco"].sum()
valor_compras_loja = f"R$ {valor_compras_loja:.2f}"
quantidade_compras_loja =df_compras_filter[df_compras_filter["loja"] == princial_loja]["preco"].count()
col21.metric("Valor compras no periodo",valor_compras_loja)
col22.metric("Quantidade de compras no periodo",quantidade_compras_loja)

st.divider()

principal_vendedor=df_compras_filter["vendedor"].value_counts().index[0]
st.markdown(f"# Campeao de vendas:  {principal_vendedor}")

valor_compras_vendedor = df_compras_filter[df_compras_filter["vendedor"]==principal_vendedor]["preco"].sum()
valor_compras_vendedor = f"R$ {valor_compras_vendedor:.2f}"
valor_comissao_vendedor = df_compras_filter[df_compras_filter["vendedor"]==principal_vendedor]["Comissao"].sum()
valor_comissao_vendedor = f"R$ {valor_comissao_vendedor:.2f}"

col31, col32 =st.columns(2)
col31.metric("Valor da compras no periodo",valor_compras_vendedor)
col32.metric("Valor da comissao no periodo", valor_comissao_vendedor)