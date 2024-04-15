import os

import matplotlib.pyplot as plt
import pandas as pd
import requests

json_url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"


class PlotDrawer:
    def __init__(self, df, *columns):
        self.df = df
        self.columns = columns

    def plot(self):
        list_coordinate = []
        for col in self.columns:
            list_coordinate.append(self.df[col])
        plt.plot(*list_coordinate)


def draw_plots(json_url, *columns):
    df = pd.read_json(json_url)
    draw = PlotDrawer(df, *columns)
    draw.plot()

    db_plots = "plots"

    if not os.path.exists(db_plots):
        os.makedirs(db_plots)

    plot_count = len([name for name in os.listdir("plots")])
    plot_file_name = str(plot_count)

    plt.savefig(os.path.join(db_plots, plot_file_name))


if __name__ == "__main__":
    draw_plots(json_url, "min", "mean", "max")
