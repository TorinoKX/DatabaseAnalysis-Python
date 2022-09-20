from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from datetime import date


class Gui(Tk):
  def __init__(self):
    super().__init__()
    self.drawMainFrame()
    
    self.drawTitleFrame()
    self.drawTitleLabel()
    self.drawNameLabel()
    self.drawInputFrame()
    self.drawReportType()
    self.drawStartDate()
    self.drawEndDate()
    self.drawDropDown()
    self.drawStartDateEntry()
    self.drawEndDateEntry()
    self.drawSubmitButton()



  def drawMainFrame(self):
    self.mainFrame = Frame(self)
    self.mainFrame.pack(fill="both", expand=True, padx=30, pady=30)
    self.mainFrame.columnconfigure(0, weight=1)
    self.mainFrame.rowconfigure(0, weight=1)
    self.mainFrame.rowconfigure(1, weight=3)


  def drawTitleFrame(self):
    self.titleFrame = Frame(self.mainFrame, )
    self.titleFrame.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
    self.titleFrame.columnconfigure(0, weight=1)
    self.titleFrame.rowconfigure(0, weight=3)
    self.titleFrame.rowconfigure(1, weight=1)

  def drawTitleLabel(self):
    self.titleLabel = Label(self.titleFrame, text="NSW Traffic Penalty Analysis Tool",
                      font=('Helvetica 25 bold'), )
    self.titleLabel.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

  def drawNameLabel(self):
    self.nameLabel = Label(self.titleFrame, text="Created by William Crane, Christopher Linnett, & Zak Cobham-Davis",
                     font=('Helvetica 10 bold'), )
    self.nameLabel.grid(row=1, column=0, padx=5, pady=5, sticky=N)

  def drawInputFrame(self):
    self.inputFrame = Frame(self.mainFrame, )
    self.inputFrame.grid(row=1, column=0, sticky=NSEW)
    self.inputFrame.columnconfigure(0, weight=1)
    self.inputFrame.columnconfigure(0, weight=2)
    self.inputFrame.rowconfigure(0, weight=1)
    self.inputFrame.rowconfigure(1, weight=1)
    self.inputFrame.rowconfigure(2, weight=1)
    self.inputFrame.rowconfigure(3, weight=2)

  def drawReportType(self):
    self.reportType = Label(self.inputFrame, text="Select a report:",
                      font=('Helvetica 15 bold'), )
    self.reportType.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    
  def drawStartDate(self):
    self.startDate = Label(self.inputFrame, text="Start Date:", font=(
    'Helvetica 15 bold'), )
    self.startDate.grid(row=1, column=0, padx=5, pady=5, sticky=W)

  def drawEndDate(self):
    self.endDate = Label(self.inputFrame, text="End Date:", font=(
    'Helvetica 15 bold'), )
    self.endDate.grid(row=2, column=0, padx=5, pady=5, sticky=W)

  def drawDropDown(self):
    reportOptions = [
        "All penalties in a period",
        "All penalties in a period involving radar/camera",
        "Distribution of penalties by code",
        "Trend of penalties over time"
    ]
    reportVar = StringVar(self.inputFrame)
    reportVar.set(reportOptions[0])
    self.reportEntry = OptionMenu(self.inputFrame, reportVar, *reportOptions)
    self.reportEntry.grid(row=0, column=1, padx=5, pady=5, sticky=E)

  def drawStartDateEntry(self):
    self.startDateEntry = DateEntry(self.inputFrame)
    self.startDateEntry.grid(row=1, column=1, padx=5, pady=5, sticky=E)
    self.startDateEntry.config(mindate=date(2010, 1, 1), maxdate=date(
    2018, 1, 1), date_pattern="dd/MM/yyyy")
    self.startDateEntry.set_date(date(2010, 1, 1))
    
  def drawEndDateEntry(self):
    self.endDateEntry = DateEntry(self.inputFrame)
    self.endDateEntry.grid(row=2, column=1, padx=5, pady=5, sticky=E)
    self.endDateEntry.config(mindate=date(2010, 1, 1), maxdate=date(
    2018, 1, 1), date_pattern="dd/MM/yyyy")
    self.endDateEntry.set_date(date(2018, 1, 1))
    
  def drawSubmitButton(self):
    self.submitButton = Button(self.inputFrame, text="Submit")
    self.submitButton.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=NSEW)