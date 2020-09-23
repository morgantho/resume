import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])


def update(event, context):

    result = table.get_item(
        Key={
            'Site': 0
        }
    )

    d = result.get('Item').get('Visits')

    data = d + 1

    table.update_item(
        Key={
            'Site': 0
        },
        UpdateExpression="set Visits = :n",
        ExpressionAttributeValues={
        ':n' : data
        },
        ReturnValues="UPDATED_NEW"
    )

    response = {
        "statusCode": 200
    }

    return response
