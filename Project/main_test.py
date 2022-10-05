import datetime
import unittest
from report import Report
from Algorithm import Algorithm
from dataset import Dataset
from main import Controller
import pandas as pd
import matplotlib.pyplot as plt

testDataFrame = pd.DataFrame([])
testFilledDataFrame = pd.DataFrame(
    pd.DataFrame([1, 2, 3], columns=['numbers']))
algorithm = Algorithm(testDataFrame)


class DatasetTests(unittest.TestCase):
    def test_loadCSVData(self):
        self.test_invalidDataFile = Dataset().loadCSVData('INVALID DATA')
        self.assertEqual(type(self.test_invalidDataFile), pd.DataFrame,
                         'Testing if dataset loadcsvdata method can accept an invalid path')

    def test_getData(self):

        self.test_gettingNonExistentData = Dataset()
        self.test_gettingNonExistentData.loadedData = pd.DataFrame([])
        self.assertEqual(type(self.test_gettingNonExistentData.getData()), pd.DataFrame,
                         'Testing the program can handle a request to return the dataset even if it is not in memory')


class ReportTest(unittest.TestCase):
    def test_getReportDataEmpty(self):
        self.assertEqual(
            type(Report(testDataFrame).getReportData()), type(pd.DataFrame([])))

    def test_getReportDataFull(self):
        self.assertEqual(
            type(Report(testFilledDataFrame).getReportData()), type(pd.DataFrame()))

    def test_generatePlot(self):
        self.test_report = Report(testDataFrame)
        self.assertEqual(type(self.test_report.generatePlot(False)), plt.Figure,
                         'Testing generatePlot method without data and no trend function')

    def test_generatePlotIsTrend(self):
        self.test_report = Report(testDataFrame)
        self.assertEqual(type(self.test_report.generatePlot(
            True)), plt.Figure, 'Testing generatePlot method without data and trend function')

    def test_generatePlotWithValues(self):
        self.test_report = Report(testFilledDataFrame)
        self.test_report.reportData = {1: 1, 2: 3, 3: 5, 4: 6}
        self.assertEqual(type(self.test_report.generatePlot(
            False)), plt.Figure, 'Testing generatePlot method with data and no trend function')

    def test_generatePlotIsTrendWithValues(self):

        self.test_report = Report(testFilledDataFrame)
        self.test_report.reportData = {1: 1, 2: 3, 3: 5, 4: 6}

        self.assertEqual(type(self.test_report.generatePlot(
            True)), plt.Figure, 'Testing generatePlot method with data and trend function')

    def test_reset(self):
        self.assertEqual(Report(testDataFrame).reset(), [],
                         'Testing reset method for clearing the dataframe')


class AlgorithmAllOffenceTest(unittest.TestCase):
    def test_allOffenceIncorrectTypeStartDate(self):
        # Incorrect type start date
        self.assertEqual(type(algorithm.allOffence("a", datetime.date(2012, 1, 1), True)), pd.DataFrame,
                         "Test incorrect type on start date input for allOffence method in Algorithm class")

    def test_allOffenceIncorrectTypeEndDate(self):
        # Incorrect type end date
        self.assertEqual(type(algorithm.allOffence(datetime.date(2012, 1, 1), "a", True)), pd.DataFrame,
                         "Test incorrect type on end date input for allOffence method in Algorithm class")

    def test_allOffenceIncorrectTypeIsMobile(self):
        # Incorrect type isMobile
        self.assertEqual(type(algorithm.allOffence(datetime.date(2012, 1, 1), datetime.date(2012, 1, 1), 3.445)),
                         pd.DataFrame, "Test incorrect type on isMobile input for allOffence method in Algorithm class")


class AlgorithmDistributionTest(unittest.TestCase):
    def test_distributionIncorrectTypeStartDate(self):
        # Incorrect type start date
        self.assertEqual(type(algorithm.distribution("a", datetime.date(2012, 1, 1), True)), dict,
                         "Test incorrect type on start date input for distribution method in Algorithm class")

    def test_distributionIncorrectTypeEndDate(self):
        # Incorrect type end date
        self.assertEqual(type(algorithm.distribution(datetime.date(2012, 1, 1), "a", True)), dict,
                         "Test incorrect type on end date input for distribution method in Algorithm class")

    def test_distributionIncorrectTypeIsMobile(self):
        # Incorrect type isMobile
        self.assertEqual(type(algorithm.distribution(datetime.date(2012, 1, 1), datetime.date(
            2012, 1, 1), 3.445)), dict, "Test incorrect type on isMobile input for distribution method in Algorithm class")


class AlgorithmInvolvingRadCam(unittest.TestCase):
    def test_involveRadCamInvalidTypeStartDate(self):
        # Incorrect type start date
        self.assertEqual(type(algorithm.involveRadCam("a", datetime.date(2012, 1, 1), True)), pd.DataFrame,
                         "Test incorrect type on start date input for involveRadCam method in Algorithm class")

    def test_involveRadCamInvalidTypeEndDate(self):
        # Incorrect type end date
        self.assertEqual(type(algorithm.involveRadCam(datetime.date(2012, 1, 1), "a", True)), pd.DataFrame,
                         "Test incorrect type on end date input for involveRadCam method in Algorithm class")

    def test_involveRadCamInvalidTypeIsMobile(self):
        # Incorrect type isMobile
        self.assertEqual(type(algorithm.involveRadCam(datetime.date(2012, 1, 1), datetime.date(2012, 1, 1), 3.445)),
                         pd.DataFrame, "Test incorrect type on isMobile input for involveRadCam method in Algorithm class")


class AlgorithmSingleOffenceTrend(unittest.TestCase):
    def test_singleOffenceTrendInvalidTypeStartDate(self):
        # Incorrect type start date
        self.assertEqual(type(algorithm.singleOffenceTrend("a", datetime.date(2012, 1, 1), True, 0)), dict,
                         "Test incorrect type on start date input for singleOffenceTrend method in Algorithm class")

    def test_singleOffenceTrendInvalidTypeEndDate(self):
        # Incorrect type end date
        self.assertEqual(type(algorithm.singleOffenceTrend(datetime.date(2012, 1, 1), "a", True, 0)),
                         dict, "Test incorrect type on end date input for singleOffenceTrend method in Algorithm class")

    def test_singleOffenceTrendInvalidTypeIsMobile(self):
        # Incorrect type isMobile
        self.assertEqual(type(algorithm.singleOffenceTrend(datetime.date(2012, 1, 1), datetime.date(
            2012, 1, 1), 3.445, 0)), dict, "Test incorrect type on isMobile input for singleOffenceTrend method in Algorithm class")

    def test_singleOffenceTrendInvalidTypeOffenceCode(self):
        # Incorrect type offenceCode
        self.assertEqual(type(algorithm.singleOffenceTrend(datetime.date(2012, 1, 1), datetime.date(2012, 1, 1), True, "a")),
                         dict, "Test incorrect type on offence code input for singleOffenceTrend method in Algorithm class")


class ControllerTest(unittest.TestCase):
    controller = Controller(False)

    def test_generateAllOffenceIsMobile(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(
            2013, 1, 1), True, 1, None)), Report, "Test for generating all offence involving mobile report")

    def test_generateAllOffenceNotMobile(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(
            2013, 1, 1), False, 1, None)), Report, "Test for generating all offence report")

    def test_generateRadCamIsMobile(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(
            2013, 1, 1), True, 2, None)), Report, "Test for generating offences involving radar/cameras and involving mobile phones report")

    def test_generateRadCamNotMobile(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(
            2013, 1, 1), False, 2, None)), Report, "Test for generating offences involving radar/cameras report")

    def test_generateDistIsMobile(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(
            2013, 1, 1), True, 3, None)), Report, "Test for generating distribution of offences involving mobile report")

    def test_generateDistNotMobile(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(
            2013, 1, 1), False, 3, None)), Report, "Test for generating distribution of offences report")

    def test_generateTrendIsMobileOffenceCode(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(
            2013, 1, 1), True, 4, 74701)), Report, "Test for generating trend of single offence involving mobiles report")

    def test_generateTrendIsMobileNoOffenceCode(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(
            2013, 1, 1), True, 4, None)), Report, "Test for generating trend of all offences report")

    def test_generateTrendNotMobileOffenceTrend(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(
            2013, 1, 1), False, 4, 74701)), Report, "Test for generating trend of one offence report")

    def test_generateTrendNotMobileNoOffenceCode(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(
            2013, 1, 1), False, 4, None)), Report, "Test for generating trend of all offences involving mobile phone report")

    def test_incorrectTypeReportID(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(
            2013, 1, 1), False, "four", None)), Report, "Test for invalid input of report ID type")

    def test_outOfRangeReportID(self):
        self.assertEqual(type(self.controller.callAlgorithm(datetime.date(2012, 1, 1), datetime.date(
            2013, 1, 1), False, -3, None)), Report, "Test for invalid input of report ID range")


unittest.main()
