from read_file import *
from constant_private import *

def main(event, context):
    
    # reading_object = reading()
    # reading_object.readFile()
    # reading_object.save()
    # rating_object = rating()
    # rating_object.readFile()
    # rating_object.save()
    # author_object = author()
    # author_object.readFile()
    # author_object.save()
    # work_object = work()
    # work_object.readFile()
    # work_object.save()
    edition_object = edition()
    edition_object.readFile()
    edition_object.save()


if __name__ == "__main__":
    main(None, None)
