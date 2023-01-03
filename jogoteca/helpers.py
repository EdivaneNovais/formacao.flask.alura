import os 
from jogoteca import app


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:#verifica se o nome da capa esta presente em nome do arquivo
            return nome_arquivo
        
    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)#pega o nome da imagem que vai ser deletada
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))#caminho pra pasta onde estão todas as imagens e nome do arquivo que quero deletar