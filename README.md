# social-network-api

API de rede social com Perfis, postagem e comentários. Usando autenticações básicas e via Token do Django Rest Framework

## Requisitos

* Python 3.6

* Django 2.2

* Django Rest Framework = 3.10

## Instalação

    > pip install -r "requirements.pip"
    > python manage.py migrate
    > python manage.py runserver


## Importação do banco de dados em JSON (Opcional)

Para importar o banco de dados do arquivo JSON acesse o endpoint _'import-database'_