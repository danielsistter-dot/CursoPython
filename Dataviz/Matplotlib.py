# import matplotlib.pyplot as plt

# meses=['Jan','Fev','Marc','Abr','Mai','Jun']
# vendas=[150,200,180,300,250,40]

# plt.figure(figsize=(8,15))
# plt.plot(
#     meses,
#     vendas,
#     marker='o',
#     linestyle='-',
#     color='blue',
#     label='Vendas'
# )

# plt.xlabel('Mês')
# plt.ylabel('Vendas')
# plt.title('Vendas do Mês')
# plt.legend()
# plt.grid(True)

# plt.show()



# import matplotlib.pyplot as plt

# vendedores =['João','Maria','Pedro','Ana']
# quantidade_vendida=[45,60,30,55]


# plt.figure(figsize=(8,5))
# plt.bar(
#     vendedores,
#     quantidade_vendida,
#     color='green'
# )

# plt.xlabel('Vendedores')
# plt.ylabel('Quantidade Vendida')
# plt.title('Quantidade Vendida Por Vendedor')

# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D

# x  = np.random.rand(50)
# y = np.random.rand(50)
# z = np.random.rand(50)

# print(x)
# print(y)

# plt.figure(figsize=(8,6))
# plt.scatter(x,y)
# plt.title('Grafico de dispersao dados aleatorios')
# plt.xlabel('Eixo x')
# plt.ylabel('Eixo y')
# plt.grid(True)
# plt.show()

# fig=plt.figure(figsize=(8,6))
# ax = fig.add_subplot(111,projection='3d')
# ax.scatter(x,y,z)
# ax.set_xlabel('Eixo x')
# ax.set_ylabel('Eixo y')
# ax.set_zlabel('Eixo z')
# ax.set_title('Grafico de dispersao 3D')
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

pontuacoes = np.random.randint(50,100,100)

plt.figure(figsize=(8,5))
plt.hist(
    pontuacoes,
    bins=10,
    color='skyblue',
    edgecolor='black'
)

plt.xlabel('Pontuaçao')
plt.ylabel('Frequencia')
plt.title('Distribuição da pontuação')


plt.show()