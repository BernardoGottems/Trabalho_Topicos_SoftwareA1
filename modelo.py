import joblib
import pandas as pd

# Carrega o modelo já treinado
modelo = joblib.load("modelo_vinho.pkl")


def prever_qualidade(alcohol, volatile_acidity, density, sulphates):

    dados = pd.DataFrame([
        {
            "alcohol": alcohol,
            "volatile acidity": volatile_acidity,
            "density": density,
            "sulphates": sulphates
        }
    ])

    resultado = modelo.predict(dados)

    return resultado[0]


# Teste manual
if __name__ == "__main__":
    teste = prever_qualidade(
        11.5,
        0.35,
        0.995,
        0.75
    )

    print("Previsão:", teste)