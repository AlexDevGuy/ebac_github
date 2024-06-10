# código de geração do gráfico

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#carregar os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

#configurar o estilo do gráfico
sns.set_style('whitegrid')

#criar a figura do gráfico
plt.figure(figsize=(10, 6))

#gerar o gráfico de linha
sns.lineplot(x='dia', y='venda', data=df, marker='o')

#configurar o título e os rótulos
plt.title('Preço da gasolina por dia', fontsize=14)
plt.xlabel('Dia', fontsize=12)
plt.ylabel('Preço (R$)', fontsize=12)

#ajustar o layout para melhor visualização
plt.tight_layout()

#salva o gráfico como uma imagem PNG
plt.savefig('gasolina.png')
plt.show()
