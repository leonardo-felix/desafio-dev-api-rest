### Pré-requisitos
* Para iniciar a aplicação, é necessário ter o python instalado e as dependências de virtualização do ambiente(virtualenv)
* Ou ter instalado o docker-compose no seu computador.

### Instruções para execução
Para a execução, a simples execução do comando: 
```
docker-compose -f docker-compose.yml up
```
e a aplicação vai iniciar por padrão no endereço http://localhost:8000/

### Endereços dos endpoints
* Criar conta: http://127.0.0.1:8000/api/contas/criar/
* Bloqueio: http://127.0.0.1:8000/api/contas/{id_conta}/bloqueio/
* Deposito: http://127.0.0.1:8000/api/contas/{id_conta}/deposito/
* extrato: http://127.0.0.1:8000/api/contas/{id_conta}/extrato/ (Para filtro por datas, especificar a query string dataInicio e/ou dataFim)
* saldo: http://127.0.0.1:8000/api/contas/{id_conta}/saldo/
* saque: http://127.0.0.1:8000/api/contas/{id_conta}/saque/

Está disponível também o arquivo do postman para requisição mais fácil, já com os metodos configurados e corpo padrão: [link postman](extra/postman.json)