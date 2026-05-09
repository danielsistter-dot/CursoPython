import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

pasta_dataset = Path(__file__).parent / "Dados"

pasta_dataset.mkdir(parents=True,exist_ok=True)

LOJAS = [
    {"estado":"SP","cidade":"São Paulo",
     "vendedores":["Ana Oliveira","Lucas Pereira"]},
     {"estado":"MG","cidade":"Belo Horizonte",
     "vendedores":["Carlos Silva","Fernanda Costa"]},
     {"estado":"RJ","cidade":"Rio de Jameiro",
     "vendedores":["Juliana Almeida","Pedro Souza"]},
     {"estado":"RS","cidade":"Porto Alegre",
     "vendedores":["Mariana Gomes","Roberto Ferreira"]},
     {"estado":"SC","cidade":"Florianopolis",
     "vendedores":["Gabriela Santos","Tiago Lima"]}    
]
PRODUTOS =[
    {"NOME": "Smartphone Samsung Galaxy","id":0,"preco":2500},
    {"NOME": "Notebook Dell Inspiriom","id":1,"preco":4500},
    {"NOME": "Tablet Apple Ipad","id":2,"preco":3000},
    {"NOME": "Smartwatch","id":3,"preco":1200},
    {"NOME": "Fone de Ouvido Sony","id":4,"preco":600},
]
FORMA_PAGTO=["cartão de Credito","Boleto","PIX","Dinheiro"]
Genero_ClientS= ["male","female"]



Compras = []
for _ in range (2000):
    LOJA = random.choice(LOJAS)
    VENDEDOR=random.choice(LOJA["vendedores"])
    PRODUTO=random.choice(PRODUTOS)
    HORA_COMPRA = datetime.now() - timedelta(
        days=random.randint(1,365),
        hours=random.randint(-5,5),
        minutes=random.randint(-30,30)
    )
    Genero_Client= random.choice(Genero_ClientS)
    NOME_CLIENTE = names.get_full_name(Genero_Client)
    FORMA_PGT = random.choice(FORMA_PAGTO)

    Compras.append({
        "data":HORA_COMPRA,
        "id_compra":0,
        "loja":LOJA["cidade"],
        "vendedor":VENDEDOR,
        "produto":PRODUTO["NOME"],
        "cliente_nome":NOME_CLIENTE,
        "cliente_genero":Genero_Client.replace("female", "feminino").replace("male", "masculino"),
        "forma_pagamento": FORMA_PGT
    })

df_compras = pd.DataFrame(Compras).set_index("data").sort_index()
df_compras["id_compra"]= [i for i in range(len(df_compras))]

df_lojas = pd.DataFrame(LOJAS)
df_produtos = pd.DataFrame(PRODUTOS)



print(df_lojas)
print(df_produtos)
print(df_compras)


df_compras.to_csv(pasta_dataset /"compras.csv", decimal=",",sep=";")
df_lojas.to_csv(pasta_dataset /"lojas.csv", decimal=",",sep=";")
df_produtos.to_csv(pasta_dataset /"produtos.csv", decimal=",",sep=";")

df_compras.to_excel(pasta_dataset / "compras.xlsx")
df_lojas.to_excel(pasta_dataset / "lojas.xlsx")
df_produtos.to_excel(pasta_dataset / "produtos.xlsx")


