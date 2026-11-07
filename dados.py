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
df['quality'] = df['quality'].apply(lambda nota: 'Alta' if nota >= 7 else 'Normal')
print(df['quality'].value_counts())


plt.figure(figsize=(8, 5))

plt.hist(df['alcohol'], bins=20, color='blue', edgecolor='black')

plt.title('Distribuição do Teor Alcoólico')
plt.xlabel('Álcool (%)')
plt.ylabel('Quantidade de Vinhos')

plt.show()