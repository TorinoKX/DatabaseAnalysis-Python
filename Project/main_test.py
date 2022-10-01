import datetime
import unittest
from report import Report
from Algorithm import Algorithm
from dataset import Dataset
import pandas as pd
import matplotlib.pyplot as plt

algorithm = Algorithm(pd.DataFrame([]))


class DatasetTests(unittest.TestCase):
    def test_loadCSVData(self):
        self.test_invalidDataFile = Dataset().loadCSVData('INVALID DATA')
        self.assertEqual(type(self.test_invalidDataFile), pd.DataFrame,
                         'Testing if dataset loadcsvdata method can accept an invalid path')

    def test_getData(self):
        
        self.test_gettingNonExistentData = Dataset()
        self.test_gettingNonExistentData.loadedData = pd.DataFrame([])
        print(self.test_gettingNonExistentData.getData())
        self.assertEqual(type(self.test_gettingNonExistentData.getData()), pd.DataFrame,
                         'Testing the program can handle a request to return the dataset even if it is not in memory')


class ReportTest(unittest.TestCase):
    def test_getReportData(self):
        pass

    def test_generatePlot(self):
        testDataframe = pd.DataFrame([])
        self.test_report = Report(testDataframe, None)
        self.assertEqual(self.test_report.generatePlot(None), "No report Data")

    def test_reset(self):
        pass


class AlgorithmTest(unittest.TestCase):

    def test_allOffence(self):
        # Incorrect type start date
        self.assertEqual(type(algorithm.allOffence("a", datetime.date(2012, 1, 1), True)), pd.DataFrame,
                         "Test incorrect type on start date input for allOffence method in Algorithm class")
        # Incorrect type end date
        self.assertEqual(type(algorithm.allOffence(datetime.date(2012, 1, 1), "a", True)), pd.DataFrame,
                         "Test incorrect type on end date input for allOffence method in Algorithm class")
        # Incorrect type isMobile
        self.assertEqual(type(algorithm.allOffence(datetime.date(2012, 1, 1), datetime.date(2012, 1, 1), 3.445)),
                         pd.DataFrame, "Test incorrect type on isMobile input for allOffence method in Algorithm class")

    def test_distribution(self):
        # Incorrect type start date
        self.assertEqual(type(algorithm.distribution("a", datetime.date(2012, 1, 1), True)), dict,
                         "Test incorrect type on start date input for distribution method in Algorithm class")
        # Incorrect type end date
        self.assertEqual(type(algorithm.distribution(datetime.date(2012, 1, 1), "a", True)), dict,
                         "Test incorrect type on end date input for distribution method in Algorithm class")
        # Incorrect type isMobile
        self.assertEqual(type(algorithm.distribution(datetime.date(2012, 1, 1), datetime.date(
            2012, 1, 1), 3.445)), dict, "Test incorrect type on isMobile input for distribution method in Algorithm class")

    def test_involveRadCam(self):
        # Incorrect type start date
        self.assertEqual(type(algorithm.involveRadCam("a", datetime.date(2012, 1, 1), True)), pd.DataFrame,
                         "Test incorrect type on start date input for involveRadCam method in Algorithm class")
        # Incorrect type end date
        self.assertEqual(type(algorithm.involveRadCam(datetime.date(2012, 1, 1), "a", True)), pd.DataFrame,
                         "Test incorrect type on end date input for involveRadCam method in Algorithm class")
        # Incorrect type isMobile
        self.assertEqual(type(algorithm.involveRadCam(datetime.date(2012, 1, 1), datetime.date(2012, 1, 1), 3.445)),
                         pd.DataFrame, "Test incorrect type on isMobile input for involveRadCam method in Algorithm class")

    def test_singleOffenceTrend(self):
        # Incorrect type start date
        self.assertEqual(type(algorithm.singleOffenceTrend("a", datetime.date(2012, 1, 1), True, 0)), dict,
                         "Test incorrect type on start date input for singleOffenceTrend method in Algorithm class")
        # Incorrect type end date
        self.assertEqual(type(algorithm.singleOffenceTrend(datetime.date(2012, 1, 1), "a", True, 0)),
                         dict, "Test incorrect type on end date input for singleOffenceTrend method in Algorithm class")
        # Incorrect type isMobile
        self.assertEqual(type(algorithm.singleOffenceTrend(datetime.date(2012, 1, 1), datetime.date(
            2012, 1, 1), 3.445, 0)), dict, "Test incorrect type on isMobile input for singleOffenceTrend method in Algorithm class")
        # Incorrect type offenceCode
        self.assertEqual(type(algorithm.singleOffenceTrend(datetime.date(2012, 1, 1), datetime.date(2012, 1, 1), True, "a")),
                         dict, "Test incorrect type on offence code input for singleOffenceTrend method in Algorithm class")


unittest.main()
