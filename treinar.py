import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

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


modelo_arvore = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

modelo_arvore.fit(X_train, y_train)


y_pred_arvore = modelo_arvore.predict(X_test)

acuracia_arvore = accuracy_score(y_test, y_pred_arvore)

print("\nAcurácia da Decision Tree:")
print(acuracia_arvore)
print(f"\nAcurácia da Decision Tree: {acuracia_arvore:.2%}")

matriz_arvore = confusion_matrix(
    y_test,
    y_pred_arvore,
    labels=["Baixa", "Alta"]
)

print("\nMatriz de Confusão da Decision Tree:")
print(matriz_arvore)


print("\nPrevisões da Decision Tree:")
print(y_pred_arvore[:20])

print("Quantidade total:", len(df))
print("Treino:", len(X_train))
print("Teste:", len(X_test))




modelo_floresta = RandomForestClassifier(
    random_state=42
)

modelo_floresta.fit(X_train, y_train)

y_pred_floresta = modelo_floresta.predict(X_test)

acuracia_floresta = accuracy_score(
    y_test,
    y_pred_floresta
)

matriz_floresta = confusion_matrix(
    y_test,
    y_pred_floresta,
    labels=["Baixa", "Alta"]
)

print("\nAcurácia da Random Forest:")
print(f"{acuracia_floresta:.2%}")

print("\nMatriz de Confusão da Random Forest:")
print(matriz_floresta)