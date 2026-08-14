# import matplotlib.pyplot as plt
# import numpy as np

# x =np.arange(1,6)
# y1=np.array([3,5,9,7,3])
# y2=np.array([1,6,2,8,4])


# fig, ax = plt.subplots(2,figsize=(8,8))

# ax[0].bar(x,y1,color='skyblue')
# ax[0].set_title('Grafico de barras')

# ax[1].plot(x,y2,marker='o',linestyle='-',color='green')
# ax[1].set_title('Grafico de linha')

# plt.show()


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# --- 1. CONFIGURAÇÕES GERAIS ---
# Define um tema do Seaborn para um visual mais limpo e profissional
sns.set_theme(style="whitegrid")
# Configura o tamanho da figura (16x8 polegadas para um dashboard lado a lado)
plt.figure(figsize=(16, 8))

# --- 2. CRIAÇÃO DE DADOS SINTÉTICOS (Consistentes com os originais) ---

# A) Dados para o Violin Plot (Distribuição de Vendas)
# Mimetiza as categorias e a distribuição da sua image_1.png
np.random.seed(42) # Para reprodutibilidade
# Simula ~50 registros por categoria com distribuições levemente diferentes
data_violin = {
    'Categoria': np.repeat(['Eletrônicos', 'Alimentos', 'Roupas', 'Livros'], 50),
    'Vendas': np.concatenate([
        np.random.normal(70, 25, 50), # Eletrônicos (mais espalhado)
        np.random.normal(55, 15, 50), # Alimentos
        np.random.normal(50, 20, 50), # Roupas
        np.random.normal(45, 12, 50)  # Livros (mais concentrado)
    ])
}
# Filtra valores negativos e extremos para limpar o visual
data_violin['Vendas'] = np.clip(data_violin['Vendas'], 10, 150)
df_violin = pd.DataFrame(data_violin)

# B) Dados para o Heatmap (Desempenho Trimestral)
# Mimetiza a matriz da sua image_0.png com o valor ~98.02
data_heatmap = {
    'Unidade': ['Matriz (SP)', 'Filial (RJ)', 'Filial (MG)', 'Matriz (SP)'],
    'Trimestre': ['T1', 'T2', 'T3', 'T4'],
    'Faturamento': [65.20, 78.45, 45.10, 98.02] # Mantendo o pico de 98.02
}
df_heatmap = pd.DataFrame(data_heatmap)
# Transforma os dados em uma matriz (pivot_table) para o heatmap
df_heatmap_pivot = df_heatmap.pivot_table(values='Faturamento', index='Unidade', columns='Trimestre')


# --- 3. GERAÇÃO DO DASHBOARD ---

# Cria o painel de subplots (1 linha, 2 colunas)
# ax é uma lista que contém os dois eixos [ax0, ax1]
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# A) Plot 1: Violin Plot (Posição ax[0])
# Especifica explicitamente ax=ax[0]
sns.violinplot(
    data=df_violin, 
    x='Categoria', 
    y='Vendas', 
    inner='quartile', # Mostra a mediana e quartis dentro do violino
    palette='muted',   # Paleta de cores suave
    ax=ax[0]
)
# Título e rótulos limpos para o primeiro gráfico
ax[0].set_title('Distribuição Estatística de Vendas por Categoria', fontsize=16)
ax[0].set_ylabel('Total de Unidades Vendidas', fontsize=12)
ax[0].set_xlabel('Categoria do Produto', fontsize=12)

# B) Plot 2: Heatmap (Posição ax[1])
# Especifica explicitamente ax=ax[1]
sns.heatmap(
    data=df_heatmap_pivot, 
    annot=True,       # Mostra os valores dentro dos blocos
    fmt=".2f",        # Formatação com 2 casas decimais (ex: 98.02)
    cmap='rocket',    # Paleta de cores (rocket é boa para escala de temperatura)
    linewidths=.5,    # Adiciona linhas sutis de separação
    ax=ax[1]
)
# Título limpo para o segundo gráfico
ax[1].set_title('Matriz de Desempenho: Faturamento Trimestral', fontsize=16)
# Remove rótulos redundantes se o DataFrame já estiver limpo
ax[1].set_ylabel('Unidade de Negócio', fontsize=12)
ax[1].set_xlabel('Trimestre Financeiro', fontsize=12)

# --- 4. AJUSTES FINAIS E SALVAMENTO ---

# Ajusta o espaçamento para evitar sobreposição de textos e títulos
plt.tight_layout()

# Título global para o dashboard (opcional, mas profissional)
plt.suptitle('Dashboard Executivo - Análise Avançada de Vendas', fontsize=20, y=1.02)

# Salva o resultado final como um arquivo JPG de alta qualidade
plt.savefig('dashboard_seaborn_unificado.jpg', dpi=300, bbox_inches='tight')

# Mostra o resultado na tela (opcional)
plt.show()

print("Dashboard Seaborn gerado com sucesso! Arquivo salvo como 'dashboard_seaborn_unificado.jpg'.")