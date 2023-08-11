import pandas as pd
from pandas import json_normalize
from datetime import datetime
from constant import *
from constant_private import *
import json

class author():
    def __init__(self, ) -> None:
        pass

    def readFile(self, ):
        file = BUCKET + INPUT + DUMP_AUTHORS_FILE
        self.dataFrame = pd.read_csv(file, sep="\t", header=None)
        self.dataFrame.columns=["type","authorId","amount", "date", "json"]
        self.dataFrame.drop(["type","amount"], axis='columns', inplace=True)
        self.dataFrame.authorId = self.dataFrame.authorId.str.extract(REGEX_AUTHOR)
        self.dataFrame.date = pd.to_datetime(self.dataFrame.date, format='ISO8601')
        print(self.dataFrame.json)

        count = 0
        authors_name = []
        for ind in self.dataFrame.index:
            json_object = json.loads(self.dataFrame['json'][ind])
            authors_name.append(self.__parse_name(json_object))
            count+=count
        self.dataFrame.drop(["json"], axis='columns', inplace=True)
        self.dataFrame['name'] = authors_name

    def __parse_any_key(self, json, key):
        if key in json :
            return json[key] 
        else:
            return ""
        
    def __parse_name(self, json) :
        result = ""
        result = self.__parse_any_key(json=json, key="name")
        return result

    def save(self):
        self.dataFrame.to_csv(BUCKET + OUTPUT + "/author.csv")