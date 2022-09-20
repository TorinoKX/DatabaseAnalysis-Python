import dataset as Dataset
from Algorithm import Algorithm
import datetime
from tkinter import *
from gui import Gui


dataset = Dataset.Dataset()

root = Gui()
root.title("NSW Traffic Penalty Analysis Tool")
root.geometry("900x500")
root.mainloop()