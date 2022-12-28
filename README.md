# formacao.flask.alura

No arquivo Python, foi importado o flask no topo do arquivo, conforme abaixo:
from flask import Flask

foi criado uma variável que receberá um novo objeto sendo instanciado, conforme o código abaixo:
from flask import Flask
app = Flask(__name__)

O código abaixo para rodar sua aplicação:
app.run()

foi criado uma pasta chamada templates e em seguida crei um arquivo HTML dentro dela com o conteúdo html (no curso utilizamos o nome lista.html

utilizei o render_template para mostrar a página criada:
@app.route('/inicio')
def ola():
    return render_template('lista.html');

mostrando jogos do servidor:

Com a diretiva do flask para usar um conteúdo dinâmico e modifiquei o título Jogoteca conforme abaixo:
<h1>{{ titulo }}</h1>


No arquivo jogoteca passei mais um parâmetro para o render_template, que será o conteúdo que será utilizado no HTML, abaixo:
@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Jogos')

Dentro de ola foi criado uma lista de jogos, essa lista foi passada como parâmetro do render_template: abaixo:
def ola():
    lista = ['Tetris', 'Skyrim', 'Crash']
    return render_template('lista.html', titulo='Jogos', jogos=lista)

No HTML deletei as tags <tr>, deixando apenas uma e modifique para pegar o nome do jogo dinamicamente, utilizando o jinja para escrever Python em HTML, abaixo:
{% for jogo in jogos %}    
                <tr>
                    <td>{{ jogo }}</td>
                </tr>
{% endfor %}

então nessa aula adicionamos um pouco mais de vida no nosso site adicionando realmente uma aparência, um estilo novo para ele, então ele está bem mais bonito do que estava na aula passada e fizemos isso através da adição do “bootstrap.css”, assim criamos essa pasta “static”, onde colocamos o bootstrap, então a pasta "static" é padronizada de acordo com Flask para colocarmos estilos CSS.

Também que existia vários trechos de códigos duplicados nos arquivos “novo.html” e “lista.html”, para dinamizarmos um pouco mais criamos a pasta “template.html” em que colocamos tudo aquilo que fosse comum nos códigos HTML.

Fizemos um sistema de herança em que a “lista.html” herda do template.html aquilo que é duplicado, aquilo que é um código que acaba aparecendo tanto no “novo.html” quanto no “lista.html”, fizemos isso a partir dessas diretivas e desses comandos extends e block do Flask, isso é bem interessante, acabou dinamizando bastante o código.

E por final viemos até o “template.html” e vimos que colocar URLs, colocar endereços completos no template não é interessante, porque a hierarquia da aplicação, pode ficar cada vez mais complexa conforme o projeto avança. Então aprendemos um pouco sobre essa url_for(), que é uma função que nos ajuda a encontrar caminhos de arquivos que precisamos encontrar.

No caso do projeto da Jogoteca, nós utilizamos um recurso do Flask chamado Flash. Esse recurso funciona com a utilização de cookies do navegador e nos permite mostrar mensagens curtas de forma eficiente na interface da nossa aplicação.Para poder mostrar a mensagem na nossa página da aplicação é necessário alterar os templates HTML com a adição de um bloco de código já fornecido pela Documentação do Flask:
 
{% with messages = get_flashed_messages() %}
            {% if messages %} 
                <ul id="messages" class="list-unstyled">
                {% for message in messages %}
                    <li class="alert alert-success">{{ message }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}

O que aprendi:

Como definir as primeiras rotas da aplicação através do @app.route.
Como integrar linguagem Python e HTML através do Flask e começar a utilizar os nossos primeiros templates de estruturação da aplicação.
Como inicializar, pela primeira vez, uma aplicação feita em Flask através do app = Flask(__name__).
Como adicionar conteúdos dinâmicos através do delimitadores do Jinja2.
Como pegar dados do servidor.
Como mostrar os atributos na view.Como criar itens para nossa aplicação através do formulário do navegador.
Como montar formulários e capturar suas informações utilizando o Flask.
O que é e como resolver o método POST no servidor.
Como fazer redirecionamento de páginas através da função redirect().
Como utilizar o bootstrap para estilizar nossa página.
Como reutilizar trechos do template.
Como gerar URLs dinâmicas.
Como fazer redirecionamento de páginas através da função redirect().
Como utilizar o bootstrap para estilizar nossa página.
Como reutilizar trechos do template.
Como gerar URLs dinâmicas.

