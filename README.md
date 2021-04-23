# Rodando o projeto
- Clone o repositorio,
- Instale as dependências com `pip install -r requirements.txt`
- Execute as migrações com `python manage.py migrate`
- crie um usuário com `python manage.py createsuperuser`
- execute o projeto com `python manage.py runserver 0.0.0.0:8000`
- acesse o link `127.0.0.1:8000/admin/` e entre com usuario e senha cadastrado acima
- no menu acesse a opção Token e clique em add token para gerar um token para usar na autenticação da api 

