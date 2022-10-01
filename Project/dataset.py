import pandas as pd


class Dataset:
    def __init__(self):
        self.loadedData = self.loadCSVData("data\penalty_data_set_2.csv")

    def loadCSVData(self, CSVDataFile):
        """
        It takes a file path as an argument, opens the file, reads the file, and returns a pandas
        dataframe
        
        :param CSVDataFile: The path to the CSV file you want to load
        :return: A dataframe
        """
        try:
            with open(CSVDataFile, 'r', encoding='utf-8') as csvData:
                CSVDataFrame = pd.read_csv(csvData, low_memory=False)
                return CSVDataFrame
        except: 
            print('You have not provided a valid file path to the csv file')
            return pd.DataFrame([])

    def getData(self):
        """
        If the data is already loaded, return it. Otherwise, print a message and return an empty
        dataframe.
        :return: A dataframe
        """
        if not self.loadedData.empty:
            return self.loadedData
        else:
            print('No Dataset exists in memory to be returned')
            return pd.DataFrame([])
