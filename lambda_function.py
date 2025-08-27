import json
import boto3 

# Make sure this is the name of your currently deployed endpoint
ENDPOINT_NAME = "sagemaker-xgboost-2025-08-27-09-37-05-508"

# Create a client to connect to SageMaker
sagemaker_runtime = boto3.client('sagemaker-runtime')

def lambda_handler(event, context):
    try:
        # The API Gateway sends data as a string in the 'body'
        body = json.loads(event['body'])
        data = body['data']
        
        # Invoke the SageMaker endpoint
        response = sagemaker_runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType='text/csv',
            Body=data
        )
        
        # The result is returned in the 'Body' of the response
        prediction = response['Body'].read().decode('utf-8')
        
        # Return a successful response
        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            'body': json.dumps({'prediction': float(prediction)})
        }
    except Exception as e:
        # Return an error response
        return {
            'statusCode': 500,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            'body': json.dumps({'error': str(e)})
        }
    