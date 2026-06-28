import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv(r"C:\Users\User\OneDrive\Área de Trabalho\udemyPython\Dataviz\dados\Pedidos.csv")


plt.figure(figsize=(8,6))
df.groupby('Regiao')['Unidades'].sum().plot(kind='bar',color='skyblue')
plt.title('Quantidade de unidades vendidas por regiao')
plt.xlabel('Regiao')
plt.ylabel('Total de unidades')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(8,6))
df['Item'].value_counts().plot(kind='pie',autopct='%1.1f%%',startangle=90)
plt.title('Distribuiçao das vendas por item')
plt.axis('equal')
plt.show()


plt.figure(figsize=(8,6))
plt.scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color='orange'
)
plt.title('Relação entre preço unitario e Quantidade')
plt.xlabel('Preço Unitario')
plt.ylabel('Quantidade de unidades')
plt.grid(True)
plt.show()



df['DataPedido'] =pd.to_datetime(df['DataPedido'])

plt.figure(figsize=(10,6))
df.groupby('DataPedido')['Unidades'].sum().plot(kind='line',marker='o',color='green')
plt.title('Quantidade de unidades vendidas ao longo do tempo')
plt.xlabel('Data do Pedido')
plt.ylabel('Total de Unidades Vendidas')
plt.grid(True)
plt.show()

pivot =df.pivot_table(
    index='Estado',
    columns='Regiao',
    values='Unidades',
    aggfunc='sum',
    fill_value=0
)
plt.figure(figsize=(10,6))
pivot.plot(kind='bar',stacked=True)
plt.title('Quantidade de Unidades vendidas por estado em cada regiao')
plt.xlabel('Estado')
plt.ylabel('Total de unidades vendidas')
plt.legend(title='Regiao',loc='upper left',bbox_to_anchor=(1.05,1))
plt.xticks(rotation=45)
plt.show()



