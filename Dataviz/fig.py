import matplotlib.pyplot as plt
import numpy as np

x =np.arange(1,6)
y1=np.array([3,5,9,7,3])
y2=np.array([1,6,2,8,4])


fig, ax = plt.subplots(2,figsize=(8,8))

ax[0].bar(x,y1,color='skyblue')
ax[0].set_title('Grafico de barras')

ax[1].plot(x,y2,marker='o',linestyle='-',color='green')
ax[1].set_title('Grafico de linha')

plt.show()