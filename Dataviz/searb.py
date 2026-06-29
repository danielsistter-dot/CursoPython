import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# empresas = ['Empresa A', 'Empresa B','Empresa C','Empresa D']
# trimestres=['T1','T2','T3','T4']

# dados=np.random.rand(4, 4)*100

# df=pd.DataFrame(
#     dados,
#     columns=trimestres,
#     index=empresas
# )

# print(df)

# plt.figure(figsize=(8,6))
# sns.heatmap(df,annot=True,cmap='coolwarm',fmt='.2f')
# plt.title('Preço de ações por trimestre')
# plt.xlabel('Trimestre')
# plt.ylabel('Empresa')
# plt.show()


# data ={
#     'Preco':[20,25,30,18,22],
#     'Quantidade':[100,120,90,110,105],
#     'Receita':[2000,3000,2700,1980,2310]
# }

# df=pd.DataFrame(data)
# print(df)

# sns.set(style='ticks')
# sns.pairplot(df,diag_kind='kde')
# plt.suptitle('Relação entre preço, Qunatidade e Receita',y=1.02)
# plt.show()


categorias = ['Eletronicos','Roupas','Alimentos','Livros']
vendas ={
    'Categoria':np.random.choice(categorias,1000),
    'Vendas':np.random.normal(loc=50,scale=20,size=1000)
}

df=pd.DataFrame(vendas)
print(df)

plt.figure(figsize=(8,6))
sns.violinplot(
    x='Categoria',
    y='Vendas',
    data=df,
    palette='muted'
)
plt.title ('Distribuição de vendas por categoria')
plt.xlabel('Categoria')
plt.ylabel('Vendas')
plt.show()