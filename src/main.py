from read_file import *
from threading import Thread
from constant_private import *

def main(event, context):
    
    reading_object = reading(1)
    edition_object = edition(2)
    rating_object = rating(3)
    author_object = author(4)
    work_object = work(5)
    work_object.run()
    author_object.run()
    edition_object.run()
    reading_object.run()
    rating_object.run()
    ""


if __name__ == "__main__":
    main(None, None)
