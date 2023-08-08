import boto3
from read_file import reading
from constant_private import *


def main(event, context):
    
    reading_object = reading()
    reading_object.readFile()
    reading_object.save()
    return {
        'statusCode': 200,
        'body': "Finished openlibrary lambda"
    }


if __name__ == "__main__":
    main(None, None)

