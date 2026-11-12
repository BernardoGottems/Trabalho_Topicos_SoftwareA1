import os

import pandas as pd
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from modelo import prever_qualidade


app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('data', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
COLUNAS_OBRIGATORIAS = [
    'alcohol',
    'volatile acidity',
    'density',
    'sulphates'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analise')
def analise():
    return render_template('analise.html')

@app.route('/resultados')
def resultados():
    return render_template('resultados.html')

@app.route('/prever', methods=['POST'])
def prever():
    try:
        alcohol = float(request.form['alcohol'])
        volatile_acidity = float(request.form['volatile_acidity'])
        density = float(request.form['density'])
        sulphates = float(request.form['sulphates'])

    except (ValueError, KeyError):
        return render_template(
            'resultados.html',
            mensagem='Erro: preencha todos os campos com valores numéricos válidos.'
        )

    resultado = prever_qualidade(
        alcohol,
        volatile_acidity,
        density,
        sulphates
    )

    return render_template('resultados.html', resultado=resultado)


@app.route('/upload', methods=['POST'])
def upload():
    arquivo = request.files.get('arquivo')

    if arquivo is None or arquivo.filename == '':
        return render_template(
            'analise.html',
            mensagem='Nenhum arquivo selecionado.'
        )

    nome_arquivo = secure_filename(arquivo.filename)

    if not nome_arquivo.lower().endswith('.csv'):
        return render_template(
            'analise.html',
            mensagem='Erro: envie apenas arquivos CSV.'
        )

    try:
        dados = pd.read_csv(arquivo, sep=',')

    except pd.errors.EmptyDataError:
        return render_template(
            'analise.html',
            mensagem='Erro: o arquivo CSV não possui dados.'
        )

    except pd.errors.ParserError:
        return render_template(
            'analise.html',
            mensagem='Erro: o arquivo CSV possui um formato inválido.'
        )

    except UnicodeDecodeError:
        return render_template(
            'analise.html',
            mensagem='Erro: não foi possível ler o arquivo CSV.'
        )

    colunas_ausentes = [
        coluna for coluna in COLUNAS_OBRIGATORIAS
        if coluna not in dados.columns
    ]

    if colunas_ausentes:
        return render_template(
            'analise.html',
            mensagem=f'Erro: o arquivo não possui as seguintes colunas obrigatórias: {", ".join(colunas_ausentes)}.'
        )

    caminho = os.path.join(
        app.config['UPLOAD_FOLDER'],
        nome_arquivo
    )

    arquivo.seek(0)
    arquivo.save(caminho)

    quantidade_linhas = len(dados)
    quantidade_colunas = len(dados.columns)

    return render_template(
        'analise.html',
        mensagem=f'Arquivo recebido: {nome_arquivo} | Registros: {quantidade_linhas} | Colunas: {quantidade_colunas}'
    )

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)