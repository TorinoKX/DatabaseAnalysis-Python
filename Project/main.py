import dataset as Dataset
from Algorithm import Algorithm
from report import Report
from gui import Gui


class Controller():
    def __init__(self):
        self.dataset = Dataset.Dataset()
        self.root = Gui(self)
        self.root.mainloop()

    def callAlgorithm(self, startDate, endDate, isMobile, reportID, offenceCode):
        """
        It takes in a start date, end date, isMobile, reportID, and offenceCode and then calls the
        appropriate algorithm and then calls the appropriate report function
        
        :param startDate: the start date of the period you want to look at
        :param endDate: the end date of the period you want to look at
        :param isMobile: boolean
        :param reportID: 1, 2, 3, 4
        :param offenceCode: the offence code of the offence you want to search for
        """
        self.report = None
        if reportID == 1:
            output = Algorithm(self.dataset.getData()).allOffence(
                startDate, endDate, isMobile)
        if reportID == 2:
            output = Algorithm(self.dataset.getData()).involveRadCam(
                startDate, endDate, isMobile)
        if reportID == 3:
            output = Algorithm(self.dataset.getData()).distribution(
                startDate, endDate, isMobile)
            # print(output)
        if reportID == 4:
            output = Algorithm(self.dataset.getData()).singleOffenceTrend(
                startDate, endDate, isMobile, offenceCode)
            # print(output)
        self.report = Report(output, self.root)
        if reportID == 3:
            self.root.resultsPlotWindow(
                self.report.generatePlot(isTrend=False))
        if reportID == 4:
            self.root.resultsPlotWindow(self.report.generatePlot(isTrend=True))
        if (reportID == 1 or reportID == 2):
            self.root.resultsTableWindow(self.report.getReportData())


program = Controller()
