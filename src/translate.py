import json
import decimalencoder
import todoList


def translate(event, context):
    # create a response
    key = event['pathParameters']['id']
    language = event['pathParameters']['language']
    item = todoList.translate_item(key, language)
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
