import pandas as pd
from datetime import datetime
from constant import *
from constant_private import *
from threading import Thread

class reading(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num
        print("Thread num: " + str(num))

    def run(self):
        self.__readFile()
        self.__save()

    def __readFile(self, ):
        file = BUCKET + INPUT + DUMP_READING_FILE
        self.dataFrame = pd.read_csv(file, sep="\t", header=None)
        self.dataFrame.columns=["worksId","booksId", "status", "date"]
        self.dataFrame.worksId = self.dataFrame.worksId.str.extract(REGEX_WORKS)
        self.dataFrame.booksId = self.dataFrame.booksId.str.extract(REGEX_BOOKS)
        self.dataFrame.date = pd.to_datetime(self.dataFrame.date, format='%Y-%m-%d')

    def __save(self):
        self.dataFrame.to_json(BUCKET + OUTPUT + "/json/reading.json", orient="records")
        print(str(self.num) + " finished: " + str(len(self.dataFrame.index)))
        