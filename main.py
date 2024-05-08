import os
import cProfile
import matplotlib.pyplot as plt
import pandas as pd

json_url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
class PlotDrawer:
    def __init__(self, df):
        self.df = df

    def draw_plot(self, column1, column2):
        plt.figure(figsize=(10, 5))
        plt.plot(self.df[column1], self.df[column2])
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.title(f"{column1} vs {column2}")
        plt.grid(True)
        plt.show()

    def save_plot(self, column1, column2, folder="plots"):
        plt.figure(figsize=(10, 5))
        plt.plot(self.df[column1], self.df[column2])
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.title(f"{column1} vs {column2}")
        plt.grid(True)
        plt.savefig(f"{folder}/{column1}_vs_{column2}.png")
        plt.close()


def draw_plots(json_file):
    df = pd.read_json(json_file)
    plot_drawer = PlotDrawer(df)
    columns = df.columns.tolist()
    if not os.path.exists("plots"):
        os.makedirs("plots")
    paths = []
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            plot_drawer.save_plot(columns[i], columns[j])
            paths.append(f"plots/{columns[i]}_vs_{columns[j]}.png")
    return paths


df = pd.read_json(json_url)
statistics = df.describe()
print(statistics)


if __name__ == '__main__':
    draw_plots(json_url)
    # cProfile.run('draw_plots(json_url)')