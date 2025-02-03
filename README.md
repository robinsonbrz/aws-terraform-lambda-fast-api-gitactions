# Projeto Lambda Python Fast Api, Terraform e CI / CD






```
git@github.com:robinsonbrz/aws-terraform-lambda-fast-api-gitactions.git

cd aws-terraform-lambda-fast-api-gitactions
```

```
python -m venv .venv

source .venv/bin/activate

python -m pip install --upgrade pip

pip install -r src/requirements.txt

pip freeze

python src/app.py
```

Executando o projeto localmente

```
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000 --log-level debug
```


___
- Executa todos os linters e flake8.
```bash
make lint
```
___
- Executa apenas um teste de coverage e pytest.
```bash
make test
```
___
- Pre commit. Executa os linters e executa um teste de coverage e pytest.
```bash
make pre
```


flake8: Flake8 é uma ferramenta de linting de código para Python. Ele analisa seu código em busca de erros potenciais, inconsistências estilísticas (que o Black pode não detectar) e violações de práticas recomendadas comuns (com base no PEP 8


```
flake8 ./src:
```

black: Black é um formatador de código muito popular e opinativo para Python.

```
black ./src
```



isort: isort é uma ferramenta que classifica automaticamente suas importações Python em ordem alfabética

```
isort ./src:
```





Executando testes


Testes com cobertura
```
pytest --cov ./src -v 
```

Exportando testes para o formato html
```
python -m pytest --cov-report html --cov ./src
```

```
pytest --cov ./src -v && python -m pytest --cov-report html --cov ./src
```


Criando um bucket pelo AWS Cli para armazenar o estado do terraform

```
aws s3api create-bucket \     
  --bucket nome-unico-lambda \
  --region us-east-1

```

No arquivo main.tf substituir o nome do bucket pelo nome-unico-lambda, utilizado anteriormente


```
cd infra-lambda

terraform init

terraform fmt

terraform apply

# --auto-approve  não pede confirmação "yes"
# terraform apply --auto-approve  
```






# aws-terraform-lambda-fast-api-gitactions