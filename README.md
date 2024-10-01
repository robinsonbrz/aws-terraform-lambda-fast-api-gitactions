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

```
cd infra-lambda

terraform init

terraform fmt

terraform apply

# --auto-approve  não pede confirmação "yes"
# terraform apply --auto-approve  
```






# aws-terraform-lambda-fast-api-gitactions