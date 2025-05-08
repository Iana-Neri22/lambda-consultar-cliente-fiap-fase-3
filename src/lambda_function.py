import json
import logging
import secrets
import string

from src.gateway.cliente_gateway import get_cliente_by_cpf

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        logger.info('Recuperando dados do cliente')
        logger.info('Raw event received: %s', json.dumps(event))
        
        # Handle both direct Lambda invocation and API Gateway requests
        if 'body' in event:
            # API Gateway request
            body = json.loads(event.get('body', '{}'))
        else:
            # Direct Lambda invocation
            body = event
            
        logger.info('Parsed body: %s', json.dumps(body))
        cpf = body.get('cpf')
        logger.info('Extracted CPF: %s', cpf)
        
        if not cpf:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "CPF parameter is required in the request body"
                })
            }
            
        cliente = get_cliente_by_cpf(cpf)
        if not cliente:
            return {
                "statusCode": 404,
                "body": json.dumps({
                    "error": "Cliente not found"
                })
            }
        
        response = {
            "statusCode": 200,
            "headers": {'Content-Type': 'application/json'},
            "body": json.dumps({"cliente": cliente})
        }
        
        logger.info('Success')
        return response
        
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Invalid JSON in request body"
            })
        }
    except Exception as e:
        logger.error('Error')
        raise