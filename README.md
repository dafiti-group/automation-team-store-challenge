# Dafiti

API Rest de Produtos (Marketing)

### Arquitetura da Aplicação

1. Toda a aplicação foi desenvolvida em Python utilizando o microframework Flask.
2. Foi criada uma estrutura redundante (2 APIs - Considerando um cenário de alta disponibilidade) utilizando o NGINX como Load Balancer (Na regra padrão de balanceamento utilizando o algoritmo Round Robin).
3. Deploy da API utilizando o Gunicorn.
4. Banco de Dados: PostgreSQL 12.
5. Toda arquitetura foi desenvolvida utilizando Docker.
6. A API possui cache utilizando o Redis.
9. A API possui autentição via JWT.
8. Toda a aplicação está coberta por Testes Unitários.
9. No diretório doc-postman, há uma collection do Postman para testes.

### Como executar a aplicação?

#### Build 
```
docker-compose build
```

#### Subir as aplicações
```
docker-compose up -d
```

### Como executar os testes?
```
python -m unittest discover -s <path>/tests -t <path>/tests
```

### Sugestões de Melhorias

1. [Segurança] Em termos de segurança, além do JWT, utilizar o CORS para fazer a restrição da origem das requisições.
2. [Monitoramento] Para agilizar e mitigar por completo o monitoramento da aplicação, seria interessante utilizar o Elastic APM. Dessa forma, seria possível fazer a indexação dos logs e análise da performance dos requests para encontrar possíveis problemas na aplicação.
3. [Deploy] Para a automatização do Deploy já com a análise do código, seria interessante utilizar o Jenkins com a integração via Docker Hub. Dessa forma, já teria o build automatizado da imagem Docker conforme o commit no repositório do GitHub, Bitbucket etc.
4. [Testes] Em um cenário de aplicação em produção, seria interessante realizar testes de stress. Uma ferramenta de sugestão é o Artillery.