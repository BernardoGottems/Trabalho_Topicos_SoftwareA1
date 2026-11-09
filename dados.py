import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data/winequality-red.csv')

#define as colunas que serão usadas no projeto
colunas_aceitas = ['alcohol','volatile acidity', 'density', 'sulphates', 'quality']
df = df[colunas_aceitas]
print(df.head())


#mostra a diferença de antes e depois da limpeza
print(f"Tamanho antes da limpeza: {df.shape}")
df = df.dropna()
df = df.drop_duplicates()
print(f"Tamanho após limpeza: {df.shape}")

#altera as notas em número para apenas alta ou normal
df['quality'] = df['quality'].apply(lambda nota: 'Alta' if nota >= 7 else 'Baixa')
print(df['quality'].value_counts())


plt.figure(figsize=(8, 5))

plt.hist(df['alcohol'], bins=20, color='blue', edgecolor='black')

plt.title('Distribuição do Teor Alcoólico')
plt.xlabel('Álcool (%)')
plt.ylabel('Quantidade de Vinhos')

plt.savefig('static/grafico_alcool.png', bbox_inches='tight')


acidez_alta =  df[df['quality'] == 'Alta']['volatile acidity']
acidez_baixa = df[df['quality'] == 'Baixa']['volatile acidity']

plt.figure(figsize=(8, 5))
plt.boxplot([acidez_alta, acidez_baixa], tick_labels=['Alta', 'Baixa'])

plt.title('Acidez Volátil por Qualidade')
plt.xlabel("Qualidade do Vinho")
plt.ylabel("Acidez Volátil")
plt.savefig('static/grafico_acidez.png', bbox_inches='tight')


vinhos_alta = df[df['quality'] == 'Alta']
vinhos_baixa = df[df['quality'] == 'Baixa']

plt.figure(figsize=(8, 5))
plt.scatter(vinhos_baixa['density'], vinhos_baixa['alcohol'], color='red', label='Baixa', alpha=0.5)
plt.scatter(vinhos_alta['density'], vinhos_alta['alcohol'], color='green', label='Alta', alpha=0.5)

plt.title('Relação: Densidade vs Álcool')
plt.xlabel('Densidade')
plt.ylabel('Álcool (%)')
plt.legend()
plt.savefig('static/grafico_dispersao.png', bbox_inches='tight')