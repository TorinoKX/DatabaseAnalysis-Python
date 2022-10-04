import datetime
import unittest
from report import Report
from Algorithm import Algorithm
from dataset import Dataset
from main import Controller
import pandas as pd
import matplotlib.pyplot as plt

testDataFrame = pd.DataFrame([])
algorithm = Algorithm(testDataFrame)


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
        self.assertEqual(
            type(Report(testDataFrame).getReportData()), type(pd.DataFrame([])))

    def test_generatePlot(self):
        self.test_report = Report(testDataFrame)
        self.assertEqual(type(self.test_report.generatePlot('')), plt.Figure)

    def test_reset(self):
        self.assertEqual(Report(testDataFrame).reset(), [])


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

class ControllerTest(unittest.TestCase):
    controller = Controller(False)

    def test_generateAllOffenceIsMobile(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(2013, 1, 1), True, 1, None)), Report, "Test for generating all offence report")

    def test_generateAllOffenceNotMobile(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(2013, 1, 1), False, 1, None)), Report, "Test for generating all offence report")
    
    def test_generateRadCamIsMobile(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(2013, 1, 1), True, 2, None)), Report, "Test for generating all offence report")
    
    def test_generateRadCamNotMobile(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(2013, 1, 1), False, 2, None)), Report, "Test for generating all offence report")
    
    def test_generateDistIsMobile(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(2013, 1, 1), True, 3, None)), Report, "Test for generating all offence report")
    
    def test_generateDistNotMobile(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(2013, 1, 1), False, 3, None)), Report, "Test for generating all offence report")
    
    def test_generateTrendIsMobileOffenceCode(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(2013, 1, 1), True, 4, 74701)), Report, "Test for generating all offence report")
    
    def test_generateTrendIsMobileNoOffenceCode(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(2013, 1, 1), True, 4, None)), Report, "Test for generating all offence report")
    
    def test_generateTrendNotMobileOffenceTrend(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(2013, 1, 1), False, 4, 74701)), Report, "Test for generating all offence report")
    
    def test_generateTrendNotMobileNoOffenceCode(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(2013, 1, 1), False, 4, None)), Report, "Test for generating all offence report")
    
    def test_incorrectTypeReportID(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(2013, 1, 1), False, "four", None)), Report, "Test for generating all offence report")
    
    def test_outOfRangeReportID(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(2013, 1, 1), False, -3, None)), Report, "Test for generating all offence report")
    
unittest.main()
