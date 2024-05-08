import unittest
from main import PlotDrawer
import pandas as pd
import os

class TestPlotDrawer(unittest.TestCase):

    def setUp(self):
        self.data = {
            'column1': [1, 2, 3, 4, 5],
            'column2': [5, 8, 30, 40, 12]
        }
        self.df = pd.DataFrame(self.data)
        self.plot_drawer = PlotDrawer(self.df)

    def test_draw_plot(self):
        self.plot_drawer.draw_plot('column1', 'column2')

    def test_save_plot(self):
        folder = 'test_plots'
        if not os.path.exists(folder):
            os.makedirs(folder)
        self.plot_drawer.save_plot('column1', 'column2', folder)
        self.assertTrue(os.path.exists(f"{folder}/column1_vs_column2.png"))

        if os.path.exists("test_plots"):
            for file in os.listdir(folder):
                os.remove(os.path.join(folder, file))
            os.rmdir(folder)

if __name__ == '__main__':
    unittest.main()
