import boto3
from read_file import *
from constant_private import *


def main(event, context):
    
    # reading_object = reading()
    # reading_object.readFile()
    # reading_object.save()
    # rating_object = rating()
    # rating_object.readFile()
    # rating_object.save()
    work_object = work()
    work_object.readFile()
    # work_object.save()


if __name__ == "__main__":
    main(None, None)
