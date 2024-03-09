import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import HandleFiles as hfile

# Z = np.array([35,24,15])
# mylabels = ["apples", "banana", "orange"]
# plt.pie(Z, labels=mylabels)
# plt.show()

class DataVisualizeError(Exception):
    pass

class VisualizeData():
    def __init__(self):
        self.data = None # list of numeric values
        self.labels = None # list of str values
        self.file_name = None

    def set_data(self, data: list) -> None:
        self.data = data

    def set_labels(self, labels: list) -> None:
        self.labels = labels
    
    def create_pie(self):
        try:
            data = np.array(self.data)
            pie_labels = self.labels

            plt.pie(data, labels=pie_labels, autopct=f"%1.1f%%")
            title = input("Enter a title: ")
            self.file_name = title
            plt.savefig(title)
        except Exception as ex:
            raise DataVisualizeError("Data not visualized: ", ex)


# new_viz = VisualizeData()
# new_viz.set_data([100,200,300,200,200,100])
# new_viz.set_labels(["1","2","3","4","5","6"])
# new_viz.create_pie()
