import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    copy_source = {
      'Bucket': 'austin-pe-ques2',
      'Key': 'hi.txt'
        }
    bucket = s3.Bucket('akash-peassignement-1')
    bucket.copy(copy_source, 'hi-copy.txt')
  
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
