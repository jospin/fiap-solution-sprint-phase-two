import pandas as pd
from pandas import json_normalize
from datetime import datetime
from constant import *
from constant_private import *
import re
import json
from threading import Thread

class edition(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num
        print("Thread num: " + str(num))

    def run(self):
        self.__readFile()
        self.__save()

    def __readFile(self, ):
        file = BUCKET + INPUT + DUMP_EDITIONS_FILE
        self.dataFrame = pd.read_csv(file, sep="\t", header=None, nrows=800000)
        self.dataFrame.columns=["type","booksId","amount", "date", "json"]
        self.dataFrame.drop(["type","amount"], axis='columns', inplace=True)
        self.dataFrame.booksId = self.dataFrame.booksId.str.extract(REGEX_BOOKS)
        self.dataFrame.date = pd.to_datetime(self.dataFrame.date, format='ISO8601')
        title = []
        subjects = []
        authors = []
        created = []
        isnb10 = []
        isnb13 = []
        for ind in self.dataFrame.index:
            json_object = json.loads(self.dataFrame['json'][ind])
            title.append(self.__parse_any_key(json_object, 'title'))
            subjects.append(self.__parse_array(json_object, "subjects"))
            authors.append(self.__parse_authors(json_object))
            isnb13.append(self.__parse_array(json_object, "isbn_13"))
            isnb10.append(self.__parse_array(json_object, "isbn_10"))
            created.append(self.__parse_created(json_object))
        self.dataFrame.drop(["json"], axis='columns', inplace=True)
        self.dataFrame['title'] = title
        self.dataFrame['subjects'] = subjects
        self.dataFrame['authors'] = authors
        self.dataFrame['isnb10'] = isnb10
        self.dataFrame['isnb13'] = isnb13
        self.dataFrame['created'] = created

    def __parse_any_key(self, json, key):
        if key in json :
            return json[key] 
        else:
            return ""
            
    def __parse_array(self, json, key) :
        result = ""

        arrayValue = self.__parse_any_key(json=json, key=key)
        # delim = "|"
        # result = delim.join([str(value) for value in arrayValue])
        return arrayValue

    def __parse_created(self, json) :
        result = ""
        created_json = self.__parse_any_key(json=json, key="created")
        result = self.__parse_any_key(json=created_json, key="value")
        return pd.to_datetime(result, format='ISO8601')
    
    def __parse_authors(self, json) :
        result = ""
        authors_object = self.__parse_any_key(json=json, key="authors")
        # delim = "|"
        try: 
            result = [re.search(REGEX_AUTHOR, str(auth['key'])).group() for auth in authors_object]
        except:
            print("Error to pase author")
        return result

    def __save(self):
        self.dataFrame.to_json(BUCKET + OUTPUT + "/json/edition.json", orient="records")
        print(str(self.num) + " finished: " + str(len(self.dataFrame.index)))
        ""