import boto3
from read_file import readings
from constant_private import *


def main(event, context):
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    
    reading_object = readings(s3_client)
    reading_object.readFile()
    reading_object.save()
    return {
        'statusCode': 200,
        'body': "Finished openlibrary lambda"
    }


if __name__ == "__main__":
    main(None, None)

