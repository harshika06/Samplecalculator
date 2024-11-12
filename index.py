import json

def handler(event, context):
    # Extract query parameters
    operation = event.get('queryStringParameters', {}).get('operation')
    num1 = float(event.get('queryStringParameters', {}).get('num1', 0))
    num2 = float(event.get('queryStringParameters', {}).get('num2', 0))

    # Perform operation
    result = 0
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Division by zero'})
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid operation'})
        }

    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }
