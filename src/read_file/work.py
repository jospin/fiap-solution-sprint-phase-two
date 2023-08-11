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
        self.dataFrame = pd.read_csv(file, sep="\t", header=None, nrows=5)
        self.dataFrame.columns=["type","worksId","amount", "date", "json"]
        self.dataFrame.drop(["type","amount"], axis='columns', inplace=True)
        # self.output = pd.DataFrame(columns=["worksId","date","title"])
        # self.output.worksId = self.dataFrame.worksId.str.extract(REGEX_WORKS)
        # self.output.date = pd.to_datetime(self.dataFrame.date, format='ISO8601')
        self.dataFrame.worksId = self.dataFrame.worksId.str.extract(REGEX_WORKS)
        self.dataFrame.date = pd.to_datetime(self.dataFrame.date, format='ISO8601')
        print(self.dataFrame.json)

        count = 0
        title = []
        subjects = []
        authors = []
        for ind in self.dataFrame.index:
            # print(self.dataFrame['json'][ind])
            json_object = json.loads(self.dataFrame['json'][ind])
            print(json_object)
            title.append(self.__parse_any_key(json_object, 'title'))
            subjects.append(self.__parse_subject(json_object))
            subjects.append(self.__parse_authors(json_object))
            count+=count
        self.dataFrame.drop(["json"], axis='columns', inplace=True)
        self.dataFrame['title'] = title
        self.dataFrame['subjects'] = subjects

    def __parse_any_key(self, json, key):
        if key in json :
            return json[key] 
        else:
            return ""
        
    def __parse_subject(self, json) :
        result = ""

        subjects = self.__parse_any_key(json=json, key="subjects")
        delim = "|"
        result = delim.join([str(sbj) for sbj in subjects])
        return result
    
    def __parse_authors(self, json) :
        authors_object = self.__parse_any_key(json=json, key="authors")
        delim = "|"
        print(authors_object)
        print([str(auth) for auth in authors_object])
        # result = delim.join([str(auth['author'].str.extract(REGEX_AUTHOR)) for auth in authors_object])
        return result

    def save(self):
        # self.output.to_csv(BUCKET + OUTPUT + "/work.csv")
        self.dataFrame.to_csv(BUCKET + OUTPUT + "/work.csv")