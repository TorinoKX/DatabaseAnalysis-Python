import dataset as Dataset
from Algorithm import Algorithm
from report import Report
from gui import Gui

class Controller():
    def __init__(self):
        self.dataset = Dataset.Dataset()
        self.root = Gui(self)
        self.root.mainloop()
    
    def callAlgorithm(self,startDate, endDate, isMobile, reportID, offenceCode = 770):
      self.report = None
      if reportID == 1:
        output = Algorithm(self.dataset.getData()).allOffence(startDate, endDate, isMobile)
      if reportID == 2:
        output = Algorithm(self.dataset.getData()).involveRadCam(startDate, endDate, isMobile)
      if reportID == 3:
        output = Algorithm(self.dataset.getData()).distribution(startDate, endDate, isMobile)
        # print(output)
      if reportID == 4:
        output = Algorithm(self.dataset.getData()).singleOffenceTrend(startDate, endDate, isMobile, offenceCode)
        # print(output)
      self.report = Report(output, self.root)

    
    


program = Controller()