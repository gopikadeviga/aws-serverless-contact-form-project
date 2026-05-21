import json
import boto3

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserMessages') 

def lambda_handler(event, context):
    try:
        # Read data from API request
        data = json.loads(event['body'])
        
        # Put data into DynamoDB
        table.put_item(Item={
            'Email': data['email'],
            'Name': data['name'],
            'Message': data['message']
        })
        
        # Return success message
        return {
            'statusCode': 200,
            'body': json.dumps('Message saved successfully!')
        }
        
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Error: {str(e)}')
        }


