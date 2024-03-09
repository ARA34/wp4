import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class DataVisualizeError(Exception):
    """
    Custom Exception class to catch any potential
    exceptions in this module
    """
    pass


class VisualizeData():
    def __init__(self):
        self.data = None
        self.labels = None
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
