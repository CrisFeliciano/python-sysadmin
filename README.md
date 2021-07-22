https://t.me/joinchat/gE-PD6yUOHhiYWEx
https://github.com/Fawers/4linux-521-7762/

21 / julho / 2021
Jenkins
- servidor de automação
- open source
- tarefas de criação, teste, dist, implementação
- continuous integration (CI)

Instalação
- pacotes nativos
- docker
- sistemas com JRE

CI
- dev ágil
- agilização de tarefas demoradas
  - compilação / build
  - testes automatizados
- execuções quando atualizado
- avisos em caso de falhas
  - deploy quando sucesso

Plugins
- > 2000
  - docker, gitlab, github, etc


- fluxos em estágios
- segmentação lógica
- identificação de bottlenecks

Jobs
- tarefas gerenciadas e monitoradas
- projetos pequenos sem pipelines
- geração de pipelines

Imagem docker: jenkins/jenkins:lts-alpine

docker run --name jenkins -dip 8080:8080 jenkins/jenkins:lts-alpine
docker exec -t jenkins cat /var/jenkins_home/secrets/initialAdminPassword

pipeline de teste:
	https://gist.github.com/Fawers/1562680c797dad450ca44df946cd66ab

19 / julho / 2021
Docker
- open source
- escrito em Go
- Linux Containers (LXC)
- AuFS
  - FS em camadas
  - leitura x escrita
  - shared dirs entre containers

Imagens:
- pacote executável, leve e autônomo
- todo o necessário para executar um software
  - tools e libs do sistema
- esqueleto de um SO

Containers:
- gerados a partir de imagens
- isola o que acontece do resto do sistema
  - HOST / GUEST
- redução de conflitos
- auxilia times a executar software na "mesma" arquitetura
- =/= virtualização
- processo isolado com namespaces e chroot

hub.docker.com/explore 

pip install -r requirements.txt

import docker
client = docker.DockerClient()
client.containers.list(all=True)

sudo gpasswd -a $(whoami) docker
Depois disso ^^^ reiniciar a máquina / VM


16 / julho / 2021
- criando ambiente virtual (venv) na pasta `.venv`
python3 -m venv .venv
- ativando o ambiente virtual
. .venv/bin/activate
- perguntando pro sistema o caminho do executável do python
which python
- no VSCode:
- Ctrl + Shift + P
- Python: Select Interpreter
- Enter ...
- e aí cola o caminho que copiamos do terminal após o comando `which python`
- por fim, instalar as deps:
pip install flask pymongo

- para iniciar o mongo:
docker start mongo-sw
- ONDE mongo-sw é o nome do container. `docker ps -a` para ver o nome do container

15 / julho / 2021
Reestruturação do projeto
Na raíz do projeto:
criar pasta config
criar arquivo config/db.py
db.py:
import pymongo

cliente = pymongo.MongoClient()
db = cliente.sw

+ função setup

criar pasta naves
mover arquivo naves.py para dentro dela com o nome blueprint.py:
- no terminal:
  cd sw
  mv naves.py naves/blueprint.py
criar arquivo models.py
mover funções referentes a naves do dados.py para naves/models.py
aplicar correções: corrigir as referências a dados, cabecalho, ...

mesma coisa com personagens, veiculos, ...

criar, na pasta config, api.py
api.py:
cabecalhos = {"Content-Type": "application/json"}


14 / julho / 2021
docker run --rm -tip 27017:27017 mongo:5.0.0
docker exec -ti NOME_DO_CONTAINER mongo
para pegar o nome do container: última coluna do comando: docker ps
show dbs -> lista os dbs disponíveis

MongoDB
- banco de dados escrito em C++
- orientado a documentos (documentos JSON)
- 2009
- problemas de big data
- escala horizontalmente e verticalmente
- grandes volumes de dados desestruturados
- possuem todos os dados necessários
  - SQL: chaves estrangeiras & relacionamentos entre tabelas
  - mongo: documentos com todos os dados
    - não precisamos de JOINs
    - mais performático
    - mais custoso
    - assíncrono

Quando usar MongoDB
- coleções desestruturadas
- não muitos relacionamentos

Quando NÃO usar MongoDB


- muitos relacionamentos

Biblioteca de mongo pra python:
pip install pymongo

Executar o mongo no docker:
docker run --name mongo-sw -dip 27017:27017 mongo:5.0.0

Verificar se o container está rodando:
docker ps

### COMANDOS DOCKER PODEM PRECISAR DE sudo
sudo docker .......

13 / julho / 2021
sudo apt update
sudo apt install -y docker.io
sudo gpasswd -a $(whoami) docker
docker pull mongo:5.0.0  # <-- pode precisar de sudo

# entra na pasta do projeto
python3 -m venv venv
vscode: Ctrl + Shift + P; Python Select Interpreter; Enter ... ; Find; venv -> bin -> python
pip install flask  # no terminal do vscode / pycharm

Flask

- microframework
  - werkzeug
- micro?
  - plugins
    - sqlalchemy / peewee
    - admin
    - migrações
    - email
- motor / engine de templates
- Olá mundo em flask


run.py:v1
import flask

app = flask.Flask(__name__)  # dois underlines

@app.route("/")
def home():
    return 'Olá mundo! da 4Linux'

@app.route("/user/<int:id>")
def user(id):
    return f"Página do usuário {id}"

@app.route("/apenas-post", methods=["POST"])
def apenas_post():
    return ''

@app.route("/saudar/<nome>")  # remova /saudar e veja o que acontece
def saudar(nome):
    return f"Saudações {nome}!"

if __name__ == "__main__":  # também com 2 underlines
    app.run(debug=True)

Veículos SW: https://swapi.dev/api/vehicles
Tudão: https://swapi.dev/api/

SERVER Jenkins:
http://localhost:8080/

SERVER Lista Postman:
http://localhost:5000/

