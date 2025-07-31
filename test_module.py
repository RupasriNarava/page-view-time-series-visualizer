import unittest
import time_series_visualizer
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class DataCleaningTestCase(unittest.TestCase):
    def test_line_plot(self):
        fig = time_series_visualizer.draw_line_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)

    def test_bar_plot(self):
        fig = time_series_visualizer.draw_bar_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)

    def test_box_plot(self):
        fig = time_series_visualizer.draw_box_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)


if __name__ == "__main__":
    unittest.main()
