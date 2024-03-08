import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Z = np.array([35,24,15])
mylabels = ["apples", "banana", "orange"]
plt.pie(Z, labels=mylabels)
plt.show()

class DataVisualizeError(Exception):
    pass

class VisualizeData():
    def __init__(self):
        self.data = None # list of numeric values
        self.labels = None # list of str values

    def set_data(self, data: list) -> None:
        self.data = data

    def set_labels(self, labels: list) -> None:
        self.labels = labels
    
    def create_pie(self):
        data = np.array(data)
        pie_labels = self.labels
        plt.pie(data, labels=pie_labels)
        plt.show() # somehow store pie chart as well

