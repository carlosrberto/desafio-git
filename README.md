# Desafio Git

1 - Clonar o repositório

```
git clone git@github.com:carlosrberto/desafio-git.git
```

2 - Criar uma branch `integration` a partir de `master`

3 - Mergear a branch `back-end` em `integration`

4 - Criar um ambiente virtual para o Python `mkvirtualenv desafio-git`

5 - Instalar as dependências do Python `pip install -r requirements.txt`

6 - Rodar a aplicação `sh start.sh`

7 - Testar o **endpoint** do CEP `http://localhost:5000/consulta-cep/?cep=14056695`

## Melhorar o seviço no arquivo `server.py`

1 - Se não tiver `cep` retornar que o cep é obrigatório `jsonify(error='cep is required')`

2 - Se `r.status_code` for diferente de `200` retornar que o cep é invalido `jsonify(error='invalid cep')`

3 - Testar se funcionou

4 - **Comitar as alterações**

## Integrar com o Front-End

1 - Mergear a branch `front-end` em `integration`
2 - Criar uma rota em `/` para renderizar o html do front-end (`render_template('index.html')`)
3 - Editar o `index.htm` para acessar a **URL** correta do serviço
4 - Comitar as alterações

## Mergear `integration` em `master`

1 - De `push` nas alterações em `integration`
2 - Volte para branch `master`
3 - Mergear `integration` em `master`