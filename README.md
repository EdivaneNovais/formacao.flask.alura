# formacao.flask.alura


Foi criado uma variável que receberá um novo objeto sendo instanciado, conforme o código abaixo:
```
from flask import Flask
app = Flask(__name__)
```

O código abaixo para rodar a aplicação:

```
app.run()
```

Foi criado uma pasta chamada templates e em seguida criei um arquivo HTML dentro dela com o conteúdo html (no curso utilizamos o nome lista.html).

Utilizei o render_template para mostrar a página criada:

```
@app.route('/inicio')
def ola():
    return render_template('lista.html');
```

Com a diretiva do flask para usar um conteúdo dinâmico, modifiquei o título Jogoteca conforme abaixo:

```
<h1>{{ titulo }}</h1>
```

No arquivo jogoteca passei mais um parâmetro para o render_template, que será o conteúdo que será utilizado no HTML, abaixo:

```
@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Jogos')
```

Dentro de ola foi criado uma lista de jogos, essa lista foi passada como parâmetro do render_template.
No HTML deletei as tags  `<tr>`, deixando apenas uma e modifique para pegar o nome do jogo dinamicamente, utilizando o jinja para escrever Python em HTML.

Então adicionamos um pouco mais de vida no nosso site adicionando realmente uma aparência, um estilo novo para ele, então ele está bem mais bonito e fizemos isso através da adição do “bootstrap.css”, assim criamos essa pasta “static”, onde colocamos o bootstrap, então a pasta "static" é padronizada de acordo com Flask para colocarmos estilos CSS.

Também que existia vários trechos de códigos duplicados nos arquivos “novo.html” e “lista.html”, para dinamizarmos um pouco mais criamos a pasta “template.html” em que colocamos tudo aquilo que fosse comum nos códigos HTML.

Fizemos um sistema de herança em que a “lista.html” herda do template.html aquilo que é duplicado, aquilo que é um código que acaba aparecendo tanto no “novo.html” quanto no “lista.html”, fizemos isso a partir dessas diretivas e desses comandos extends e block do Flask, isso é bem interessante, acabou dinamizando bastante o código.

E por final viemos até o “template.html” e vimos que colocar URLs, colocar endereços completos no template não é interessante, porque a hierarquia da aplicação, pode ficar cada vez mais complexa conforme o projeto avança. Então aprendemos um pouco sobre essa `url_for()`, que é uma função que nos ajuda a encontrar caminhos de arquivos que precisamos encontrar.

No caso do projeto da Jogoteca, nós utilizamos um recurso do Flask chamado Flash. Esse recurso funciona com a utilização de cookies do navegador e nos permite mostrar mensagens curtas de forma eficiente na interface da nossa aplicação.Para poder mostrar a mensagem na nossa página da aplicação é necessário alterar os templates HTML com a adição de um bloco de código já fornecido pela Documentação do Flask:

Criamos três novas rotas ao longo dessa aula, a rota de login que nos dá um formulário que podemos colocar credenciais e fazer o login.

Colocamos uma rota que é específica só para fazer autenticação desse login, e nessa rota utilizamos o session, sendo um atributo do Flask para guardar certas informações do usuário quando ele está fazendo o login nos cookies do navegador. Ele captura essas informações e nos permite usar mais tarde, como fizemos na mensagem que colocamos também caso o login for bem-sucedido, então colocamos mensagens para interagir mais com usuário quando está usando o site.

Fizemos uma rota de logout também para podermos esquecer essa informação de usuário quando é interessante que esqueçamos, e fizemos algumas alterações nos HTMLs, o HTML de login que criamos também nessa aula, e adicionamos esse código para ser possível a mensagem, um código recomendado pela própria documentação para utilizarmos, e fizemos essa alteração também no template.


# O que foi realizado:

**Como definir as primeiras rotas da aplicação através do @app.route.**

**Como integrar linguagem Python e HTML através do Flask e começar a utilizar os nossos primeiros templates de estruturação da aplicação.**

**Como inicializar, pela primeira vez, uma aplicação feita em Flask através do app = Flask(__name__).**

**Como adicionar conteúdos dinâmicos através do delimitadores do Jinja2.**

**Como pegar dados do servidor.**

**Como mostrar os atributos na view.Como criar itens para nossa aplicação através do formulário do navegador.**

**Como montar formulários e capturar suas informações utilizando o Flask.**

**O que é e como resolver o método POST no servidor.**

**Como fazer redirecionamento de páginas através da função redirect().**

**Como utilizar o bootstrap para estilizar nossa página.**

**Como reutilizar trechos do template.**

**Como gerar URLs dinâmicas.**

**Como fazer redirecionamento de páginas através da função redirect().**

**Como utilizar o bootstrap para estilizar nossa página.**

**Como reutilizar trechos do template.**

**Como gerar URLs dinâmicas.**

**Como criar a tela de login.**

**Como guardar os dados da sessão.**

**Como deslogar a sessão.**

**Como fazer a proteção de rotas.**

**Como tornar melhor nosso fluxo de login.**

**Como controlar múltiplos usuários.**

**Entendemos que uma aplicação web deve ser capaz de persistir os dados salvos mesmo depois de reiniciar o servidor e uma forma de fazer isso é por meio da utilização de um banco de dados.**

**Aprendemos o que é um ORM e que sua utilização permite não apenas integrar a aplicação com um banco de dados, mas interagir de maneira mais eficiente com ele.**

**Utilizamos o SQLAlchemy para fazer a comunicação com o banco de dados MySQL, através da criação de models (classes) que representavam cada tabela do banco.**

**Reorganizamos o código da aplicação para tornar o desenvolvimento do projeto mais eficiente.**

**Aprendemos que o CRUD se faz presente em muitas aplicações web e que é um acrônimo às funcionalidades que toda aplicação deveria ter: Create, Read, Upload e Delete.**

**Criamos uma rota de edição para realizar o update de itens no nosso banco de dados a partir do navegador.**

**Criamos uma rota para deletar itens do banco de dados a partir do navegador.**

**Como subir arquivos de imagem para o servidor através da utilização de input do tipo file.**

**Entendemos que a vantagem de armazenar imagens em um diretório da aplicação no servidor está associada ao menor custo no uso de banco de dados.**

**Vimos que existe uma maior vantagem em criarmos nomes personalizados para cada imagem salva no servidor do que utilizar o nome de arquivo fornecido pelo usuário.**

**A utilizar Javascript para aumentar a interatividade da aplicação com o usuário.**

**Ajustamos a rota de edição para permitir a inclusão de capas de jogos para os itens da lista e mostrar a capa padrão caso ainda não exista uma capa cadastrada.**

**Entendemos do que se trata a questão de CACHE do navegador e como contornar o problema através da utilização de um timestamp nos nomes de capa de cada item.**

**Ainda quanto ao CACHE, criamos uma função de deleção de capas de jogos repetidas.**

**Melhorar a interface do código, adicionando botões na página inicial do website que levam para todas as rotas.**

**Adicionar botões de retorno para página inicial em todas as demais rotas.**

**Fazer o download do Flask WTF para implementar a validação dos formulários da aplicação.**

**Criar classes através do Flask WTF que correspondem a cada um dos formulários que temos na aplicação.**

**Alterar as rotas e templates de novo jogo, edição de jogos e login de usuário para funcionar de acordo com o Flask WTF.**

**O que é a quebra de segurança CSRF e como impedi-la utilizando o CSRF Token do Flask WTF.**

**Refatorar os arquivos do projeto para garantir máxima eficiência de desenvolvimento.**

**Ajustar a interface do website para torná-lo o mais amigável o possível à utilização do usuário.**

**Criptografar as senhas cadastradas no banco de dados com o Flask Bcrypt para impedir qualquer possibilidade de vazamento de senhas por acesso indevido ao banco de dados.**

