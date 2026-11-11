# Trabalho_Topicos_SoftwareA1



Foram testados dois modelos de classificação:

Decision Tree
Random Forest


Decision Tree: 85,61% de acurácia
Random Forest: 85,24% de acurácia

# Modelo escolhido

A Decision Tree foi escolhida como modelo final porque apresentou a maior acurácia entre os dois modelos testados, com 85,61%, contra 85,24% da Random Forest.
Além disso, a Decision Tree identificou corretamente 11 vinhos da classe Alta, enquanto a Random Forest identificou 8.
Como a base apresenta desbalanceamento entre as classes, a matriz de confusão também foi considerada na decisão, e não apenas a acurácia.



Foi definido que vinhos com quality >= 7 são classificados como qualidade Alta, enquanto os demais são classificados como qualidade Baixa.
Esse corte transforma o problema em uma classificação binária e segue o recorte definido para o tema de Qualidade de Vinhos no trabalho.