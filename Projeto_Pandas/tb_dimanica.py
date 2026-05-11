import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta

perc_comissao=0.05
colunas_analise =["loja","vendedor","produto","cliente_genero","forma_pagamento"]
colunas_numericas = ["preco","comissao"]
funcoes_agregacao = {"soma":"sum", "contagem":"count"}

caminho_datasets = "Projeto_Pandas/Dados"

df_compras = pd.read_csv(f"{caminho_datasets}/compras.csv", sep=";",decimal=",",index_col=0,parse_dates=True)
df_lojas =pd.read_csv(f"{caminho_datasets}/lojas.csv", sep=";",decimal=",", index_col=0)
df_produtos =pd.read_csv(f"{caminho_datasets}/produtos.csv", sep=";",decimal=",",index_col=0)


df_produtos =df_produtos.rename(columns={"NOME": "produto"})

df_compras =df_compras.reset_index()
df_compras = pd.merge(left=df_compras,
                      right=df_produtos[["produto","preco"]],
                      on="produto",
                      how="left"
                      )
df_compras =df_compras.set_index("data")
df_compras["comissao"]=df_compras["preco"]*perc_comissao


indice_dinamico=st.sidebar.multiselect("Selecione os indices", colunas_analise)
colunas_filtradas=[c for c in colunas_analise if not c in indice_dinamico]
coluna_dinamica=st.sidebar.multiselect("Selecione as colunas",colunas_filtradas)
valor_analise=st.sidebar.selectbox("Selecione o valor",colunas_numericas)
metrica_analise=st.sidebar.selectbox("Selecione a metrica",list(funcoes_agregacao.keys()))

if len(indice_dinamico) > 0 and len(coluna_dinamica) > 0:
    metrica = funcoes_agregacao[metrica_analise]
    compras_dinamica=pd.pivot_table(
        df_compras,
        index=indice_dinamico,
        columns=coluna_dinamica,
        values=valor_analise,
        aggfunc=metrica
    )
    compras_dinamica["Total_ Geral"]=compras_dinamica.sum(axis=1)
    compras_dinamica.loc["Total_Geral"]=compras_dinamica.sum(axis=0).to_list()

    st.dataframe(compras_dinamica)
