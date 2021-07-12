# Automation Team - Technical Challenge

# About

# theme: shoes

# Python - Django project using Vue as front-end version 1.0

1. Configuration Project

This project was made using pipenv, you can use the command above to start the virtual environment and after run the second command to install all the packages in Pipfile.lock

'''
pipenv shell
pipenv sync 
'''

2. Running the aplication

After running the pipenv sync, use the commands to start the django server
Obs. the user for django admin is chris, and password 123

'''
cd mysite
python manage.py migrate
python manage.py runserver
http://127.0.0.1:8000/shoes/
'''

3. Start the Vue app

to start Vue, open a cmd terminal and use the commands above.
Obs. it is required the node.js is installed

'''
cd vueapp\vuedjangorest
npm run serve
http://localhost:8080/
'''

## Packages

1. python == 3.8.2
2. Django==3.2.5
3. django-cors-headers==3.7.0
4. djangorestframework==3.12.4
5. pytest==6.2.4
6. pytest-django==4.4.0
7. pytest-forked==1.3.0
8. pytest-xdist==2.3.0

### API

#### Attributes:
- modelo: CharField, max_length=30
- status: CharField, choices=ShoesStatus.choices, max_length=30 
- data_de_lancamento: DateField
- marca: CharField, max_length=30
- quantidade: IntegerField, default= 10
- preco: DecimalField, max_digits=5, decimal_places=2, default=100.00
- tamanho: IntegerField, validators=[MinValueValidator(0),MaxValueValidator(50)], default=40

## Basepath: http://127.0.0.1:8000/

### API GET

*Example:*

'''
http://127.0.0.1:8000/shoes/{id}
'''

### API POST

'''
    "modelo": "testes", <- This field is required
    "status": "",
    "data_de_lancamento": "",
    "marca": "test",  <- This field is required
    "quantidade": 
'''


