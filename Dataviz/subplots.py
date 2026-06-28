import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv(r"C:\Users\User\OneDrive\Área de Trabalho\udemyPython\Dataviz\dados\Pedidos.csv")


fig, ax = plt.subplots(2 , 2 , figsize=(8,8))

df.groupby('Regiao')['Unidades'].sum().plot(kind='bar',color='skyblue',ax=ax[0,0])
ax[0,0].set_title('Quantidade de unidades vendidas por regiao')
ax[0,0].set_xlabel('Regiao')
ax[0,0].set_ylabel('Total de unidades')
ax[0,0].tick_params(axis='x', rotation=45)

df['Item'].value_counts().plot(kind='pie',autopct='%1.1f%%',startangle=90,ax=ax[0,1])
ax[0,1].set_title('Distribuiçao das vendas por item')
ax[0,1].axis('equal')



ax[1,0].scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color='orange'
)
ax[1,0].set_title('Relação entre preço unitario e Quantidade')
ax[1,0].set_xlabel('Preço Unitario')
ax[1,0].set_ylabel('Quantidade de unidades')
ax[1,0].grid(True)


df['DataPedido'] =pd.to_datetime(df['DataPedido'])

df.groupby('DataPedido')['Unidades'].sum().plot(kind='line',marker='o',color='green',ax=ax[1,1])
ax[1,1].set_title('Quantidade de unidades vendidas ao longo do tempo')
ax[1,1].set_xlabel('Data do Pedido')
ax[1,1].set_ylabel('Total de Unidades Vendidas')
ax[1,1].grid(True)

plt.tight_layout()
plt.show()