import pandas as pd

class Dataset:
    def __init__(self):
        self.loadedData = self.loadCSVData("/data/penalty_data_set_2.csv")

    def loadCSVData(CSVDataFile):
        with open(CSVDataFile, 'r', encoding='utf-8') as csvData:
           CSVDataFrame = pd.read_csv(csvData)
           return CSVDataFrame

    def getData(self):
        return self.loadedData