import pandas as pd
from datetime import datetime
from constant import *

class readings():
    def __init__(self, s3_client) -> None:
        self.s3_client = s3_client

        pass

    def readFile(self, ):
        file = INPUT + "readings/ol_dump_reading-log_2023-07-31.txt"
        response = self.s3_client.get_object(Bucket=BUCKET, Key=file)
        self.dataFrame = pd.read_csv(response.get('Body'), sep="\t", header=None)
        self.dataFrame.columns=["worksId","booksId", "status", "date"]
        self.dataFrame.worksId = self.dataFrame.worksId.str.extract(REGEX_WORKS)
        self.dataFrame.booksId = self.dataFrame.booksId.str.extract(REGEX_BOOKS)
        self.dataFrame.date = pd.to_datetime(self.dataFrame.date, format='%Y-%m-%d')
        print(self.dataFrame.dtypes)
        print(self.dataFrame)

    def save(self):
        self.s3_client.put_object(Body=self.dataFrame.to_parquet(), Bucket=BUCKET, Key=OUTPUT+"readings/reading.parquet")
        