import matplotlib.pyplot as plt


class Report():

    def __init__(self, reportData, root):
        self.root = root
        self.reportData = reportData

    def generatePlot(self):
        all_values = [x for x in self.reportData.values(
        ) if x > 0.01 * sum(self.reportData.values())]
        all_keys = [str(x) for x in self.reportData.keys(
        ) if self.reportData[x] > 0.01*sum(self.reportData.values())]

        figure = plt.figure(figsize=(5, 5), dpi=100)
        figure.add_subplot(111).bar(all_keys, all_values)
        return figure
        # axes = figure.add_axes([0,0,1,1])
        # axes.bar(all_keys, all_values)
        # axes.set_title('Insert Title Here')
        # axes.xaxis.set_label("XaxisLabel")
        # axes.yaxis.set_label("YaxisLabel")

    def reset(self):
        self.reportData = []
