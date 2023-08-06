import pandas as pd

class editions():
    def __init__(self, PATH) -> None:
        self.path = PATH
        self.file = self.path + "ol_dump_editions_latest.txt"
        pass

    def readFile(self):
        dataFrame = pd.read_csv(self.file, "\t")
        print(dataFrame)

        # print(f'Number of Lines in the file is {count}')
        # print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        # print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
        # print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)