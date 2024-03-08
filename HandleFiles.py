from pathlib import Path
import matplotlib as plt


class FileCreationError(Exception):
    pass


def save_plot():
    title = input("What is your title: ")
    plt.savefig(title)