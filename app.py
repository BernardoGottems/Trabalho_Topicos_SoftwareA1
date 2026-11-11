import os
import pandas as pd
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('data', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analise')
def analise():
    return render_template('analise.html')

@app.route('/upload', methods=['POST'])
def upload():
    arquivo = request.files.get('arquivo')

    if arquivo is None or arquivo.filename == '':
        return render_template('analise.html', mensagem='Nenhum arquivo selecionado.')

    nome_arquivo = secure_filename(arquivo.filename)

    if not nome_arquivo.lower().endswith('.csv'):
        return render_template('analise.html', mensagem='Erro: envie apenas arquivos CSV.')

    caminho = os.path.join(
        app.config['UPLOAD_FOLDER'],
        nome_arquivo
    )

    arquivo.save(caminho)

    if os.path.getsize(caminho) == 0:
        return render_template('analise.html', mensagem='Erro: o arquivo enviado está vazio.')

    try:
        dados = pd.read_csv(caminho, sep=',')

    except pd.errors.EmptyDataError:
        return render_template('analise.html', mensagem='Erro: o arquivo CSV não possui dados.')

    except pd.errors.ParserError:
        return render_template('analise.html', mensagem='Erro: o arquivo CSV possui um formato inválido.')

    except UnicodeDecodeError:
        return render_template('analise.html', mensagem='Erro: não foi possível ler o arquivo CSV.')

    quantidade_linhas = len(dados)
    quantidade_colunas = len(dados.columns)

    return render_template(
        'analise.html',
        mensagem=f'Arquivo recebido: {nome_arquivo} | Registros: {quantidade_linhas} | Colunas: {quantidade_colunas}'
    )

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
