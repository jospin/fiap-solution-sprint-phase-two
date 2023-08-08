import pandas as pd
from datetime import datetime
from constant import *
from constant_private import *

class rating():
    def __init__(self, ) -> None:
        pass

    def readFile(self, ):
        file = BUCKET + INPUT + DUMP_RATINGS_FILE
        self.dataFrame = pd.read_csv(file, sep="\t", header=None)
        self.dataFrame.columns=["worksId","booksId", "rates", "date"]
        self.dataFrame.worksId = self.dataFrame.worksId.str.extract(REGEX_WORKS)
        self.dataFrame.booksId = self.dataFrame.booksId.str.extract(REGEX_BOOKS)
        self.dataFrame.date = pd.to_datetime(self.dataFrame.date, format='%Y-%m-%d')
        print(self.dataFrame.dtypes)
        print(self.dataFrame)

    def save(self):
        self.dataFrame.to_csv(BUCKET + OUTPUT + "/rating.csv")
        