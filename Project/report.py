import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Report():

  def __init__(self, reportData, root):
    self.root = root
    self.reportData = reportData
    if type(reportData) == dict:
      self.generatePlot()
  
  def generatePlot(self):
    all_values = self.reportData.values()
    all_keys = self.reportData.keys()

    figure = plt.figure(figsize=(10,10), dpi=200)
    axes = figure.add_axes([0,0,1,1])
    axes.bar(all_keys, all_values)
    axes.set_title('Insert Title Here')
    axes.xaxis.set_label("XaxisLabel")
    axes.yaxis.set_label("YaxisLabel")
    # figure.savefig('testfigure.png', bbox_inches='tight')
  
    chart_type = FigureCanvasTkAgg(figure, self.root)
    chart_type.get_tk_widget().pack()

  def reset(self):
    self.reportData = []