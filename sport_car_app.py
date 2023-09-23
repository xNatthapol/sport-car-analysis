import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sport_car_graph import GraphPlotter
from sport_car_database import CarData


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.facade = CarFacade()
        self.title('Sport Car Analysis')
        self.screen_width = self.winfo_screenwidth() - 200
        self.screen_height = self.winfo_screenheight() - 200
        self.geometry(f'{self.screen_width}x{self.screen_height}+100+100')
        self.menu_frame = ttk.Frame(self)
        self.menu_frame.pack(fill=tk.BOTH, side=tk.TOP)
        self.menu_widget()
        self.graph_frame = ttk.Frame(self)
        self.graph_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.graph_widget()
        self.bar_plot()
        self.info_frame = tk.LabelFrame(self, text='Information')
        self.info_frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        self.info_widget()

    def menu_widget(self):
        self.bar_button = ttk.Button(self.menu_frame, text='Time-series',
                                     command=self.bar_plot)
        self.bar_button.pack(side=tk.LEFT, padx=10)
        self.pie_button = ttk.Button(self.menu_frame, text='Part-to-whole',
                                     command=self.pie_plot)
        self.pie_button.pack(side=tk.LEFT, padx=10)
        self.histogram_button = ttk.Button(self.menu_frame,
                                           text='Distribution',
                                           command=self.histogram_plot)
        self.histogram_button.pack(side=tk.LEFT, padx=10)
        self.scatter_button = ttk.Button(self.menu_frame, text='Correlation',
                                         command=self.scatter_plot)
        self.scatter_button.pack(side=tk.LEFT, padx=10)
        self.quit_button = ttk.Button(self.menu_frame, text='Exit',
                                      command=self.exit)
        self.quit_button.pack(side=tk.LEFT, padx=10)

    def graph_widget(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.canvas = FigureCanvasTkAgg(self.fig, self.graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10,
                                         pady=10)

    def info_widget(self):
        # show description of the graph
        self.info_label = ttk.Label(self.info_frame,
                                    text='Descriptive Statistics')
        self.info_label.pack(pady=5)
        column_names = self.facade.get_column_names()
        for column_name in column_names:
            frame = tk.LabelFrame(self.info_frame, text=column_name)
            frame.pack(fill=tk.BOTH, padx=10, pady=10)
            self.facade.get_descriptive(frame, column_name)

    def bar_plot(self):
        self.facade.plot_bar(self.ax, self.canvas)

    def pie_plot(self):
        self.facade.plot_pie(self.ax, self.canvas)
        self.ax.remove()
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])

    def histogram_plot(self):
        self.facade.plot_histogram(self.ax, self.canvas)

    def scatter_plot(self):
        self.facade.plot_scatter(self.ax, self.canvas)

    def exit(self):
        self.destroy()


class CarFacade:
    def __init__(self):
        self.graph = GraphPlotter()
        self.cd = CarData()

    def plot_bar(self, ax, canvas):
        ax.clear()
        self.graph.bar_plotter(ax)
        canvas.draw()

    def plot_pie(self, ax, canvas):
        ax.clear()
        self.graph.pie_plotter(ax)
        canvas.draw()

    def plot_histogram(self, ax, canvas):
        ax.clear()
        self.graph.histogram_plotter(ax)
        canvas.draw()

    def plot_scatter(self, ax, canvas):
        ax.clear()
        self.graph.scatter_plotter(ax)
        canvas.draw()

    def get_column_names(self):
        return self.cd.data.columns.drop(
            ['Car Make', 'Car Model', 'Engine Size', '0-60 Time(s)', 'Price'])

    def get_descriptive(self, frame, column_name):
        label_mean = ttk.Label(frame, text='Mean: ' + str(
            self.cd.get_mean(column_name)))
        label_mean.pack(pady=3)
        label_median = ttk.Label(frame, text='Median: ' + str(
            self.cd.get_median(column_name)))
        label_median.pack(pady=3)
        label_mode = ttk.Label(frame, text='Mode: ' + str(
            self.cd.get_mode(column_name)))
        label_mode.pack(pady=3)
        label_std = ttk.Label(frame, text='Standard Deviation: ' + str(
            self.cd.get_std(column_name)))
        label_std.pack(pady=3)
        label_max = ttk.Label(frame,
                              text='Max: ' + str(self.cd.get_max(column_name)))
        label_max.pack(pady=3)
        label_min = ttk.Label(frame,
                              text='Min: ' + str(self.cd.get_min(column_name)))
        label_min.pack(pady=3)
