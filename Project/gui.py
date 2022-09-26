from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from datetime import date
import matplotlib
matplotlib.use('TkAgg')


class Gui(Tk):
    def __init__(self, parent):
        super().__init__()
        self.title("NSW Traffic Penalty Analysis Tool")
        self.geometry("900x500")
        self.parent = parent
        self.drawMainFrame()
        self.drawMainScreen()

    def drawMainScreen(self):
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
        self.drawIsMobileInvolved()
        self.drawSubmitButton()

    def drawResultsFrame(self):
        self.resultsFrame = Frame(self.mainFrame, )
        self.resultsFrame.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

    def drawResultsTable(self, dataframe):
        h = Scrollbar(self.resultsFrame, orient="horizontal")
        h.pack(side=BOTTOM, fill=X)
        v = Scrollbar(self.resultsFrame)
        v.pack(side=RIGHT, fill=Y)

        self.resultsTable = Treeview(
            self.resultsFrame, xscrollcommand=h.set, yscrollcommand=v.set)
        self.resultsTable['columns'] = self.columns
        self.resultsTable.column("#0", width=0, stretch=NO)
        self.resultsTable.heading("#0", text="", anchor=CENTER)
        for column in self.columns:
            self.resultsTable.column(column, anchor=CENTER, width=80)
            self.resultsTable.heading(column, text=column, anchor=CENTER)

    def drawReturnButton(self):
        pass

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
        self.reportOptions = [
            "",
            "All penalties in a period",
            "All penalties in a period involving radar/camera",
            "Distribution of Penalties Grouped by Offence Code",
            "Trend of Specific Offence Code over Time"
        ]
        self.reportVar = StringVar(self.inputFrame)
        self.reportVar.set(self.reportOptions[1])
        self.reportEntry = OptionMenu(
            self.inputFrame, self.reportVar, *self.reportOptions)
        self.reportEntry.grid(row=0, column=1, padx=5, pady=5, sticky=E)

    def drawStartDateEntry(self):
        self.startDateEntry = DateEntry(self.inputFrame)
        self.startDateEntry.grid(row=1, column=1, padx=5, pady=5, sticky=E)
        self.startDateEntry.config(mindate=date(2012, 3, 1), maxdate=date(
            2018, 1, 1), date_pattern="dd/MM/yyyy")
        self.startDateEntry.set_date(date(2013, 3, 1))

    def drawIsMobileInvolved(self):
        self.mobileBool = IntVar()
        self.isMobileInvolved = Checkbutton(
            self.inputFrame, text="Limit to mobile phone usage?", variable=self.mobileBool, onvalue=1, offvalue=0)
        self.isMobileInvolved.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky=E)

    def drawEndDateEntry(self):
        self.endDateEntry = DateEntry(self.inputFrame)
        self.endDateEntry.grid(row=2, column=1, padx=5, pady=5, sticky=E)
        self.endDateEntry.config(mindate=date(2012, 3, 1), maxdate=date(
            2018, 1, 1), date_pattern="dd/MM/yyyy")
        self.endDateEntry.set_date(date(2013, 4, 1))

    def drawSubmitButton(self):
        self.submitButton = Button(
            self.inputFrame, text="Submit", command=self.submitButtonHandler)
        self.submitButton.grid(
            row=4, column=0, columnspan=2, padx=5, pady=5, sticky=NSEW)

    def submitButtonHandler(self):
        startDate = self.startDateEntry.get_date()
        endDate = self.endDateEntry.get_date()
        isMobile = self.mobileBool.get()
        reportID = self.reportOptions.index(self.reportVar.get())
        # print(f"start_date: {startDate}, end_Date: {endDate}, isMobile: {isMobile}, reportOption: {reportID}")
        self.parent.callAlgorithm(startDate, endDate, isMobile, reportID)

    def resultsWindow(self, plot):
        resultsWindow = Toplevel(self)
        resultsWindow.geometry("900x500")
        resultsWindow.title("Results")
        self.chart = FigureCanvasTkAgg(plot, resultsWindow)
        NavigationToolbar2Tk(self.chart, resultsWindow)
        self.chart.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
