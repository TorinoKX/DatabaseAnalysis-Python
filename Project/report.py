import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd


class Report():

    def __init__(self, reportData):
        self.reportData = reportData

    def getReportData(self):
        """
        It returns the reportData attribute of the object
        :return: The reportData
        """
        if not self.reportData.empty:
            return self.reportData
        else:
            return pd.DataFrame([])

    def generatePlot(self, isTrend):
        """
        It takes a boolean value, if true, the plot will be a line graph. If false, it will be a bar graph.
        
        :param isTrend: boolean
        :return: A figure object
        """
        try:
            if not isTrend:
                all_values = [x for x in self.reportData.values(
                ) if x > 0.005 * sum(self.reportData.values())]
                all_keys = [str(x) for x in self.reportData.keys(
                ) if self.reportData[x] > 0.005*sum(self.reportData.values())]
            else:
                all_values = [x for x in self.reportData.values()]
                all_keys = [str(x) for x in self.reportData.keys()]
        except:
            print("cannot access keys or values in outputted report data")
            return plt.figure()
        figure = plt.figure(figsize=(5, 5), dpi=100)
        ax = figure.add_subplot(111)
        if isTrend:
            ax.plot(all_keys, all_values, marker="s")
            ax.set(xlabel="Dates (Month/Years)", ylabel="Offence Frequency")
        else:
            ax.bar(all_keys, all_values)
            ax.set(xlabel="Offence Code", ylabel="Offence Instances")


        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        for tick in ax.get_xticklabels():
            tick.set_rotation(45)
        figure.set_tight_layout(True)
        return figure

    def reset(self):
        """
        It resets the reportData to an empty list.
        :return: The reportData list.
        """
        self.reportData = []
        return self.reportData
