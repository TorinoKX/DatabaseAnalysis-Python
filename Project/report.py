import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

class Report():

  def __init__(self, reportData, root):
    self.root = root
    self.reportData = reportData
  
  def generatePlot(self):
    all_values = self.reportData.values()
    all_keys = self.reportData.keys()

    figure = plt.figure(figsize=(5,4), dpi=100)
    axes = figure.add_axes([0,0,1,1])
    axes.bar(all_values, all_keys)
    axes.set_title('Insert Title Here')
    axes.xaxis.set_label("XaxisLabel")
    axes.yaxis.set_label("YaxisLabel")
    chart_type = FigureCanvasTkAgg(figure, self.root)
    chart_type.get_tk_widget().pack()

  def reset(self):
    self.reportData = []