import pandas as pd

# Lê o arquivo CSV já tratado pela Pessoa 2
df = pd.read_csv("data/winequality-limpo.csv")

# X = características usadas para fazer a previsão
X = df[
    [
        "alcohol",
        "volatile acidity",
        "density",
        "sulphates"
    ]
]

# y = resposta que queremos 
y = df["quality"]

print("X:")
print(X.head())

print("\ny:")
print(y.head())