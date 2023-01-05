import os 
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

class FormularioJogo(FlaskForm):#classe flaskform faz a validação
    nome = StringField('Nome do Jogo', [validators.data_required(), validators.Length(min=1, max=50)])#valida os dados da string e o comprimento dela no banco de dados
    categoria = StringField('Categoria', [validators.data_required(), validators.Length(min=1, max=40)])
    console = StringField('Console', [validators.data_required(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.data_required(), validators.Length(min=1, max=8)] )
    senha = PasswordField('Senha', [validators.data_required(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:#verifica se o nome da capa esta presente em nome_do_arquivo
            return nome_arquivo
        
    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)#pega o nome da imagem que vai ser deletada
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))#caminho pra pasta onde estão todas as imagens e nome do arquivo que quero deletar
        #O método join() serve para fazer a concatenação baseado no formato do primeiro parâmetro (app.config).