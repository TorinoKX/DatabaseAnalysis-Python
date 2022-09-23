import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

class Report():

  def __init__(self, reportData):
    self.reportData = reportData
  
  def generatePlot(self):
    all_values = self.reportData.values()
    all_keys = self.reportData.keys()

    numCols = len(self.reportData)
    numRows = max(all_values)


    f = plt.Figure(figsize=(5,4), dpi=100)
    ax = f.add_subplot((numRows, numCols, 1))

  def reset(self):
    self.reportData = []