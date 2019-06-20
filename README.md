# Github Explore
Simple exercice to fetch and save trending repos on github

## Rodar o projeto Localmente (requer python3 e pip instalados):

- Criar ambiente Virtual (usei pipenv):

`pip3 install pipenv`

... na pasta do projeto:

`pipenv shell`

- Instalar dependências

`pipenv install`

Com outro virtualenv será algo como:

`virtualenv ENV`

`source /path/to/ENV/bin/activate`

`pip3 install -r requirements.txt`

- Criar banco local:

`python manage.py makemigrations`

`python manage.py migrate`

- Criar usuário para acessar "/admin":

`python manage.py createsuperuser`

... após seguir os passos ....

- Iniciar servidor local

`pipenv run python manage.py runserver`

Rodar Testes:

`python manage.py test explorer.tests`

## Técnologias utilizadas

### Web App
    - Django: Web Framework
    - Gunicorn: Web Server
    - WhiteNoise (django-heroku): Gerenciar arquivos estáticos do Django/DRF

### Deploy
    - Github + Heroku CLI: Auto Deploy
    - SQLite3: Banco para testes em dev
    - Heroku Postgres: Banco em prod
    - Pipenv: Gerenciamento de Dependências dev/prod e Variaveis de Ambientes em dev (.env file)
    - dj_database_url: Configuração automatica dos bancos de dev/prod

### API Github
    - Requests: Consumir API Github
    - JSON: Parser

### Testes
    - Django TestCase: Testes Unitários
    - Selenium: Teste de Interface
