# Lambda Consultar Cliente - FIAP Fase 3

Este projeto contém uma função Lambda para consulta de clientes por CPF.

## Endpoint da API

A API está disponível através do API Gateway no seguinte endpoint:

```
https://we2edfldjl.execute-api.us-east-1.amazonaws.com/dev/consultar-cliente
```

## Autenticação

Para acessar a API, é necessário incluir o header de autorização:

```
authorizationToken: abc123
```

## Formato da Requisição

A requisição deve ser feita com um corpo JSON contendo o CPF do cliente:

```json
{
    "cpf": "13243546578"
}
```

## Deploy

O deploy da aplicação pode ser realizado de duas formas:

1. **Via linha de comando:**
   ```bash
   serverless deploy
   ```

2. **Via GitHub Actions:**
   - Faça push para a branch `main`
   - O deploy será executado automaticamente através do workflow configurado

## Tecnologias Utilizadas

- AWS Lambda
- API Gateway
- Serverless Framework
- GitHub Actions