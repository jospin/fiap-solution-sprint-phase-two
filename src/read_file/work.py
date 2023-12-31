import pandas as pd
from pandas import json_normalize
from datetime import datetime
from constant import *
from constant_private import *
import re
import json
from threading import Thread

class work(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num
        print("Thread num: " + str(num))

    def run(self):
        self.__readFile()
        self.__save()

    def __readFile(self, ):
        file = BUCKET + INPUT + DUMP_WORK_FILE
        self.dataFrame = pd.read_csv(file, sep="\t", header=None, nrows=700000)
        self.dataFrame.columns=["type","worksId","amount", "date", "json"]
        self.dataFrame.drop(["type","amount"], axis='columns', inplace=True)
        self.dataFrame.worksId = self.dataFrame.worksId.str.extract(REGEX_WORKS)
        self.dataFrame.date = pd.to_datetime(self.dataFrame.date, format='ISO8601')
        title = []
        subjects = []
        authors = []
        created = []
        for ind in self.dataFrame.index:
            json_object = json.loads(self.dataFrame['json'][ind])
            title.append(self.__parse_any_key(json_object, 'title'))
            subjects.append(self.__parse_subject(json_object))
            authors.append(self.__parse_authors(json_object))
            created.append(self.__parse_created(json_object))
        self.dataFrame.drop(["json"], axis='columns', inplace=True)
        self.dataFrame['title'] = title
        self.dataFrame['subjects'] = subjects
        self.dataFrame['authors'] = authors
        self.dataFrame['created'] = created

    def __parse_any_key(self, json, key):
        if key in json :
            return json[key] 
        else:
            return ""
        
    def __parse_subject(self, json) :
        result = ""

        subjects = self.__parse_any_key(json=json, key="subjects")
        return subjects

    def __parse_created(self, json) :
        result = ""
        created_json = self.__parse_any_key(json=json, key="created")
        result = self.__parse_any_key(json=created_json, key="value")
        return pd.to_datetime(result, format='ISO8601')
    
    def __parse_authors(self, json) :
        result = ""
        authors_object = self.__parse_any_key(json=json, key="authors")
        try: 
            result = [re.search(REGEX_AUTHOR, str(auth['author'])).group() for auth in authors_object]
        except:
            ""
        return result

    def __save(self):
        self.dataFrame.to_json(BUCKET + OUTPUT + "/json/work.json", orient="records")
        print(str(self.num) + " finished: " + str(len(self.dataFrame.index)))