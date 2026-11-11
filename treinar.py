import pandas as pd
from sklearn.model_selection import train_test_split

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


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Quantidade total:", len(df))
print("Treino:", len(X_train))
print("Teste:", len(X_test))