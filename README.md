# Automation Team - Technical Challenge

---

# Aplicação

Desenvolvido um site com o intuito de mostrar ao usuário o melhor produto para ele efetuar a compra. 
Pode ser escolhido produtos entre as lojas Dafiti e Zattini. Foi utilizado a tecnologia de scraping,
por meio do selenium. A extração dos dados fora feita nos sites das lojas listadas, porém direcionado
a produtos especificos, que são os tênis das marcas Adidas e Nike! No site, também, é possível ver a concorrencia entre as lojas.
Concorrência em quantas vezes a loja foi vantajosa e qual das lojas possui mais promoções.

---

# Instruções

A aplicação está hospedada no heroku, podendo ser acessada e interagida por (https://api-compare-dafiti.herokuapp.com/).

O frontend foi desenvolvido com Django Template e a APi com Python e Django Rest Framework.

A aplicação contém os endpoints documentadados com Swagger e podendo ser acessado por (https://api-compare-dafiti.herokuapp.com/docs/)

Se desejar rodar o projeto local, use os comandos:

- `docker-compose build`

- `docker-compose up`

