import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from pandastable import Table
from tkinter import *
from tkinter.ttk import *
from tkcalendar import DateEntry
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
        """
        It draws the main screen of the GUI.
        """
        self.drawTitleFrame()
        self.drawTitleLabel()
        self.drawNameLabel()
        self.drawInputFrame()
        self.drawReportType()
        self.drawOffenceCode()
        self.drawStartDate()
        self.drawEndDate()
        self.drawCodeSelection()
        self.drawDropDown()
        self.drawStartDateEntry()
        self.drawEndDateEntry()
        self.drawIsMobileInvolved()
        self.drawSubmitButton()

    def drawMainFrame(self):
        """
        It creates a main frame to contain the menu, packs it, and then configures it.
        """
        self.mainFrame = Frame(self)
        self.mainFrame.pack(fill="both", expand=True, padx=30, pady=30)
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)
        self.mainFrame.rowconfigure(1, weight=3)

    def drawTitleFrame(self):
        """
        It creates a frame in the main frame for title and names.
        """
        self.titleFrame = Frame(self.mainFrame, )
        self.titleFrame.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)
        self.titleFrame.columnconfigure(0, weight=1)
        self.titleFrame.rowconfigure(0, weight=3)
        self.titleFrame.rowconfigure(1, weight=1)

    def drawTitleLabel(self):
        """
        The function draws a label containing the title of the program on the titleFrame.
        """
        self.titleLabel = Label(self.titleFrame, text="NSW Traffic Penalty Analysis Tool",
                                font=('Helvetica 25 bold'), )
        self.titleLabel.grid(row=0, column=0, padx=5, pady=5, sticky=NS)

    def drawNameLabel(self):
        """
        This function creates a label that displays the names of the creators of the program.
        """
        self.nameLabel = Label(self.titleFrame, text="Created by William Crane, Christopher Linnett, & Zak Cobham-Davis",
                               font=('Helvetica 10 bold'), )
        self.nameLabel.grid(row=1, column=0, padx=5, pady=5, sticky=N)

    def drawInputFrame(self):
        """
        It creates a frame in the main frame for inputs, then configures the rows and columns of the frame.
        """
        self.inputFrame = Frame(self.mainFrame, )
        self.inputFrame.grid(row=1, column=0, sticky=NSEW)
        self.inputFrame.columnconfigure(0, weight=1)
        self.inputFrame.columnconfigure(0, weight=2)
        self.inputFrame.rowconfigure(0, weight=1)
        self.inputFrame.rowconfigure(1, weight=1)
        self.inputFrame.rowconfigure(2, weight=1)
        self.inputFrame.rowconfigure(3, weight=2)

    def drawReportType(self):
        """
        The function draws a label on the inputFrame that says "Select a report:".
        """
        self.reportType = Label(self.inputFrame, text="Select a report:",
                                font=('Helvetica 15 bold'), )
        self.reportType.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    def drawOffenceCode(self):
        """
        It creates a label called "Offence Code" and places it in the inputFrame.
        """
        self.offenceCode = Label(self.inputFrame, text="Offence Code:", font=(
            "Helvetica 15 bold"))
        self.offenceCode.grid(row=1, column=0, padx=5, pady=5, sticky=W)

    def drawStartDate(self):
        """
        The function draws a label on the GUI that says "Start Date:"
        """
        self.startDate = Label(self.inputFrame, text="Start Date:", font=(
            'Helvetica 15 bold'), )
        self.startDate.grid(row=2, column=0, padx=5, pady=5, sticky=W)

    def drawEndDate(self):
        """
        The function draws a label on the GUI that says "End Date"
        """
        self.endDate = Label(self.inputFrame, text="End Date:", font=(
            'Helvetica 15 bold'), )
        self.endDate.grid(row=3, column=0, padx=5, pady=5, sticky=W)

    def drawCodeSelection(self):
        """
        It creates an entry box that only allows numbers to be entered
        """
        #Testing
        def testInput(changedVar):
            if changedVar.isdigit():
                return True
            elif changedVar == "":
                return True
            else:
                return False

        self.codeSelectionText = StringVar()

        self.codeSelection = Entry(
            self.inputFrame, textvariable=self.codeSelectionText, state=DISABLED)
        self.codeSelection.grid(row=1, column=1, padx=5, pady=5, sticky=E)
        reg = self.inputFrame.register(testInput)

        self.codeSelection.config(validate="key", validatecommand=(reg, "%P"))

    def dropdownUpdated(self, event):
        """
        If the user selects the 4th option in the dropdown menu, enable the codeSelection entry box.
        Otherwise, disable it.
        
        :param event: The event that called this function
        """
        if (self.reportOptions.index(event) == 4):
            self.codeSelection.config(state=NORMAL)
        else:
            self.codeSelection.config(state=DISABLED)

    def drawDropDown(self):
        """
        It creates a dropdown menu with the options "All penalties in a period", "All penalties in a
        period involving radar/camera", "Distribution of Penalties Grouped by Offence Code", and "Trend
        of Specific Offence Code over Time".
        """

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
            self.inputFrame, self.reportVar, *self.reportOptions, command=self.dropdownUpdated)
        self.reportEntry.grid(row=0, column=1, padx=5, pady=5, sticky=E)

    def drawStartDateEntry(self):
        """
        It creates a DateEntry widget and places it in the inputFrame.
        """
        self.startDateEntry = DateEntry(self.inputFrame)
        self.startDateEntry.grid(row=2, column=1, padx=5, pady=5, sticky=E)
        self.startDateEntry.config(mindate=date(2012, 1, 1), maxdate=date(
            2017, 11, 1), date_pattern="dd/MM/yyyy")
        self.startDateEntry.set_date(date(2012, 1, 1))

    def drawEndDateEntry(self):
        """
        It creates a DateEntry widget and places it in the inputFrame
        """
        self.endDateEntry = DateEntry(self.inputFrame)
        self.endDateEntry.grid(row=3, column=1, padx=5, pady=5, sticky=E)
        self.endDateEntry.config(mindate=date(2012, 1, 1), maxdate=date(
            2017, 11, 1), date_pattern="dd/MM/yyyy")
        self.endDateEntry.set_date(date(2017, 11, 1))

    def drawIsMobileInvolved(self):
        """
        It creates a checkbox that allows the user to limit the search to mobile phone usage
        """
        self.mobileBool = IntVar()
        self.isMobileInvolved = Checkbutton(
            self.inputFrame, text="Limit to mobile phone usage?", variable=self.mobileBool, onvalue=1, offvalue=0)
        self.isMobileInvolved.grid(
            row=4, column=0, columnspan=2, padx=5, pady=5, sticky=E)

    def drawSubmitButton(self):
        """
        The function creates a button that calls the submitButtonHandler function when clicked
        """
        self.submitButton = Button(
            self.inputFrame, text="Submit", command=self.submitButtonHandler)
        self.submitButton.grid(
            row=5, column=0, columnspan=2, padx=5, pady=5, sticky=NSEW)

    def submitButtonHandler(self):
        """
        It takes the user input from the GUI and passes it to the algorithm
        """
        startDate = self.startDateEntry.get_date()
        endDate = self.endDateEntry.get_date()
        isMobile = self.mobileBool.get()
        reportID = self.reportOptions.index(self.reportVar.get())
        offenceCode = self.codeSelectionText.get()
        # print(f"start_date: {startDate}, end_Date: {endDate}, isMobile: {isMobile}, reportOption: {reportID}")
        self.parent.callAlgorithm(startDate, endDate, isMobile, reportID, int(
            offenceCode) if offenceCode else None)

    def resultsPlotWindow(self, plot):
        """
        It takes a plot and puts it onto a canvas in a new window
        
        :param plot: The plot that is to be displayed in the new window
        """
        resultsPlotWindow = Toplevel(self)
        resultsPlotWindow.geometry("900x500")
        resultsPlotWindow.title("Results")
        self.chart = FigureCanvasTkAgg(plot, resultsPlotWindow)
        NavigationToolbar2Tk(self.chart, resultsPlotWindow)
        self.chart.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        #Closes originally created plot as it has been put onto a canvas. Allows program to correctly exit when closing windows.
        plt.close('all')

    def resultsTableWindow(self, df):
        """
        It creates a new window, and then creates a table in that window using the dataframe that was
        passed to the function.
        
        :param df: the dataframe to be displayed
        """
        resultsTableWindow = Toplevel(self)
        resultsTableWindow.geometry("900x500")
        resultsTableWindow.title("Results")
        pt = Table(resultsTableWindow, dataframe=df,
                   showtoolbar=False, showstatusbar=True)
        pt.show()
