# Trabalho_Topicos_SoftwareA1 — Análise e Previsão da Qualidade de Vinhos

Aplicação web desenvolvida em **Flask**, **Pandas**, **Matplotlib** e **Scikit-learn** para análise exploratória via upload de arquivos CSV e classificação da qualidade de vinhos com Machine Learning.

## 1. Problema e Fonte dos Dados

* **Pergunta do projeto:** É possível prever se um vinho terá qualidade sensorial alta a partir de suas propriedades físico-químicas básicas?
* **Dataset:** *Wine Quality Dataset* (Cortez et al., 2009), disponibilizado pelo repositório **UCI Machine Learning**.
* **Base utilizada no treinamento:** O modelo preditivo disponível na aplicação foi treinado previamente com a base de vinho tinto (`data/winequality-red.csv`). A página de análise aceita o envio tanto da base de vinho tinto quanto de vinho branco (`winequality-white.csv`), atualizando dinamicamente a amostra dos dados e os gráficos.

## 2. Instalação e Execução

* **Instalar as dependências do projeto:**
  ```bash
  pip install -r requirements.txt
  ```

* **Treinar e gerar o modelo novamente (opcional, caso `modelo_vinho.pkl` já exista):**
  ```bash
  python treinar.py
  ```

* **Iniciar o servidor Flask:**
  ```bash
  python app.py
  ```

* **Acessar a aplicação:** abra o navegador em `[http://127.0.0.1:5000](http://127.0.0.1:5000)`.

## 3. Esquema do CSV e Definição de Variáveis (X e y)

Para o upload na rota `/upload`, a aplicação aceita arquivos `.csv` delimitados por vírgula (`,`) ou ponto e vírgula (`;`) que contenham obrigatoriamente as seguintes colunas:

| Coluna             | Papel         | Tipo                  | Descrição e Relevância no Problema                                                            |
|:-------------------|:--------------|:----------------------|:----------------------------------------------------------------------------------------------|
| `alcohol`          | Entrada ($X$) | Numérico (%)          | Teor alcoólico; contribui para o corpo, estrutura e equilíbrio sensorial do vinho.            |
| `volatile acidity` | Entrada ($X$) | Numérico (g/dm³)      | Acidez volátil; níveis elevados conferem sabor avinagrado indesejado e reduzem a nota.        |
| `density`          | Entrada ($X$) | Numérico (g/cm³)      | Densidade do líquido; reflete o equilíbrio entre açúcar residual e álcool após a fermentação. |
| `sulphates`        | Entrada ($X$) | Numérico (g/dm³)      | Sulfatos; atuam como antioxidante e antimicrobiano, preservando o frescor da bebida.          |
| `quality`          | Alvo ($y$)    | Categórico (derivado) | Nota sensorial original (0 a 10), convertida para classificação binária (`Alta` ou `Baixa`).  |

Foi definido que vinhos com `quality >= 7` são classificados como qualidade **Alta**, enquanto os demais são classificados como qualidade **Baixa**. Esse corte transforma o problema em uma classificação binária e segue o recorte estabelecido para o tema, permitindo separar exemplares considerados superiores da média comum do mercado.

## 4. Limpeza de Dados e Achados da Análise Exploratória

* **Tratamento aplicado (`dados.py`):** O arquivo CSV original é preservado na pasta `data/`. Durante o processamento, selecionam-se apenas as 5 colunas relevantes, removem-se registros com valores ausentes (`dropna()`) e linhas duplicadas (`drop_duplicates()`), reduzindo a base de vinho tinto de `1599` registros originais para `[TOTAL_APOS_LIMPEZA]` registros únicos.
* **Três achados principais nas visualizações:**
  * **Distribuição do Teor Alcoólico (Histograma):** A maior concentração dos vinhos encontra-se entre `9,5%` e `11%` de álcool, apresentando assimetria à direita com poucos rótulos ultrapassando `13%`.
  * **Acidez Volátil por Qualidade (Boxplot):** Vinhos de qualidade `Alta` apresentam mediana e amplitude de acidez volátil visivelmente menores que os de qualidade `Baixa`, confirmando que o excesso de acidez volátil penaliza a avaliação sensorial.
  * **Densidade vs. Álcool (Dispersão):** Observa-se uma relação inversamente proporcional entre densidade e teor alcoólico; os vinhos de qualidade `Alta` concentram-se predominantemente na faixa de maior teor alcoólico e menor densidade.

## 5. Treinamento, Comparação e Escolha do Modelo

Os dados limpos foram divididos com `train_test_split` na proporção **80% para treino** (`[QTD_TREINO]` registros) e **20% para teste** (`[QTD_TESTE]` registros), utilizando `random_state=42` e estratificação (`stratify=y`) para manter a proporção original das classes (`[QTD_BAIXA]` Baixa / `[QTD_ALTA]` Alta).

Foram testados dois modelos de classificação:
* **Decision Tree (`max_depth=4`):** **85,61%** de acurácia
* **Random Forest:** **85,24%** de acurácia

### Modelo escolhido

A **Decision Tree** foi escolhida como modelo final porque apresentou a maior acurácia entre os dois modelos testados, com **85,61%**, contra **85,24%** da Random Forest. Além disso, a Decision Tree identificou corretamente **11 vinhos da classe Alta**, enquanto a Random Forest identificou **8**. Como a base apresenta desbalanceamento entre as classes, a matriz de confusão também foi considerada na decisão, e não apenas a acurácia.

### Limitações

* **Desbalanceamento de classes:** A classe `Baixa` representa aproximadamente `[PORCENTAGEM_CLASSE_BAIXA]%` da base, o que faz o modelo acertar com muito mais facilidade vinhos comuns do que identificar vinhos de qualidade `Alta` (gerando falsos negativos na classe minoritária).
* **Escopo físico-químico:** O modelo avalia apenas quatro propriedades químicas e foi treinado exclusivamente com vinho tinto, não capturando variáveis como safra, casta da uva ou diferenças estruturais de vinhos brancos.

## 6. Equipe e Responsabilidades

* **[Nome do Integrante 1]:** Desenvolvimento da aplicação web em Flask (`app.py`), rotas de upload/previsão, validação de arquivos e templates HTML/CSS.
* **[Nome do Integrante 2]:** Tratamento, limpeza e análise exploratória dos dados com Pandas e geração das visualizações com Matplotlib (`dados.py`).
* **[Nome do Integrante 3]:** Separação treino/teste, treinamento, comparação dos modelos de Machine Learning e exportação do modelo (`treinar.py` e `modelo.py`).

## 7. Referências e Ferramentas Utilizadas

* Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). *Modeling wine preferences by data mining from physicochemical properties*. Decision Support Systems, 47(4), 547-553.
* Bibliotecas Python: Flask, Pandas, Matplotlib, Scikit-learn e Joblib.
* Apoio de Inteligência Artificial (Google Gemini) utilizado para revisão de integração entre Flask e Matplotlib, tratamento de separadores CSV e estruturação da documentação.