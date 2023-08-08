import pandas as pd
from pandas import json_normalize
from datetime import datetime
from constant import *
from constant_private import *
import json

class work():
    def __init__(self, ) -> None:
        pass

    def readFile(self, ):
        file = BUCKET + INPUT + DUMP_WORK_FILE
        self.dataFrame = pd.read_csv(file, sep="\t", header=None, nrows=30)
        self.dataFrame.columns=["type","worksId","amount", "date", "json"]
        self.dataFrame.drop(columns=['type','amount'], axis=1, inplace=True)
        self.dataFrame.worksId = self.dataFrame.worksId.str.extract(REGEX_WORKS)
        self.dataFrame.date = pd.to_datetime(self.dataFrame.date, format='ISO8601')
        # self.dataFrame.json = pd.read_json(self.dataFrame.json)
        for ind in self.dataFrame.index:
            # json_object = json.load(self.dataFrame['json'][ind])
            print(self.dataFrame['json'][ind])
        
        # self.dataFrame.booksId = self.dataFrame.booksId.str.extract(REGEX_BOOKS)
        # self.dataFrame.date = pd.to_datetime(self.dataFrame.date, format='%Y-%m-%d')
        # print(self.dataFrame.dtypes)
        # print(self.dataFrame)

    def save(self):
        self.dataFrame.to_csv(BUCKET + OUTPUT + "/work.csv")
        