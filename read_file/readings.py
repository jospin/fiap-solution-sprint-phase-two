import pandas as pd
from datetime import datetime
from constant import *

class readings():
    def __init__(self, PATH) -> None:
        self.path = PATH
        self.file = self.path + "ol_dump_reading-log_2023-07-31.txt"
        pass

    def readFile(self):
        self.dataFrame = pd.read_csv(self.file, sep="\t", header=None)
        self.dataFrame.columns=["worksId","booksId", "status", "date"]
        self.dataFrame.worksId = self.dataFrame.worksId.str.extract(REGEX_WORKS)
        self.dataFrame.booksId = self.dataFrame.booksId.str.extract(REGEX_BOOKS)
        self.dataFrame.date = pd.to_datetime(self.dataFrame.date, format='%Y-%m-%d')
        print(self.dataFrame.dtypes)
        print(self.dataFrame)

    def save(self, OUTPUT):
        self.dataFrame.to_parquet(OUTPUT+"readings.parquet")