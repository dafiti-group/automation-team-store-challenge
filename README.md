# Rodando o projeto

- Clone o repositorio,
- Instale as dependências com `pip install -r requirements.txt`
- Execute as migrações com `python manage.py migrate`
- crie um usuário com `python manage.py createsuperuser`
- execute o projeto com `python manage.py runserver 0.0.0.0:8000`
- acesse o link `127.0.0.1:8000/admin/` e entre com usuario e senha cadastrado acima
- no menu acesse a opção Tokens e clique em 'adicionar token' para gerar um token para usar na autenticação da api
- use um programa para acesar os endpoints, como o insomnia por exemplo;
- endpoints:
  `http://127.0.0.1:8000/api/v1/marcas/`
  `http://127.0.0.1:8000/api/v1/produtos/`
- para acessar a API precisa informar a autenticação do tipo bearer prefix `token` e o token obtido nos passos
  anteriores
- primeiramente cadastre as marcas enviando um post `http://127.0.0.1:8000/api/v1/marcas/` com o seguinte json:

```
  {
    "nome": "marca teste"
  }
```

- depois cadastre os produtos enviando um post `http://127.0.0.1:8000/api/v1/produtos/` com o seguinte json:

```
  {
    "nome": "Produto teste",
    "sku": "123",
    "descricao": "Produto de testes",
    "quantidade": 10,
    "preco": "10.00",
    "tipo": "normal",	
    "marca": "marca teste 2"
  }
```

- para criar um produto novo altere o campo 'SKU', se usar um SKU já cadastrado o item será atualizado.
- para obter um unico registro use metodo get `http://127.0.0.1:8000/api/v1/produtos/<uuid>`
- para excluir um registro use metodo delete `http://127.0.0.1:8000/api/v1/produtos/<uuid>`

para fins de teste, a ligação entre o produto e a marca, se dá pelo slug da marca que é gerado automaticamente, e não
pelo id de referencia

o campo 'total_estoque' do get do produto é auto calculado com base na quantidade * preço