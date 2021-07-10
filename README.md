# Promofit
## API para uma loja online de Moda e Lifestyle

### Aplicação

https://promofit.herokuapp.com/api/

### Documentação

[Documentação completa da API](https://documenter.getpostman.com/view/11375427/Tzm6mbit#2a113bdf-7aa3-4535-8ac8-69d6de8b9124)

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com/), [Python 3.9](https://www.python.org/downloads/)

### Rodando o Back-End (Servidor)

```bash
# Clone este repositório
$ git clone https://github.com/yurilimak9/automation-team-store-challenge

# Acesse a pasta do projeto no terminal/cmd
$ cd automation-team-store-challenge

# Instale a virtual env
$ python3 -m venv venv

# Ative a virtual end
$ source venv/bin/activate

# Crie um arquino .env na raiz do projeto com os seguintes valores
SECRET_KEY=django-insecure-zrks1carhziyxh_&n$z*0e=(fs0rda-+a0=o7l&v!h$xvf_i7p
DEBUG=True

# instale as dependências
$ pip install -r requirements-dev.txt

# Faça o mapeamento dos modelos
$ python manage.py makemigrations user product

# Suba as migrações para o banco de dados
$ python manage.py migrate

# Popule o banco de dados com dados de teste
$ python manage.py loaddata user address department category brand product

# Execute a aplicação
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse <http://127.0.0.1:8000>
```

### Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://python.org/)
- [Django](https://djangoproject.com/)
- [Django Rest Framework](https://django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io)
- [Requests](https://docs.python-requests.org)
- [Pillow](https://pillow.readthedocs.io)
- [dj-database-url](https://pypi.org/project/dj-database-url)
- [Python-Decouple](https://pypi.org/project/python-decouple/)

### Autor

[Yuri Gonçalves Lima](https://github.com/yurilimak9)
