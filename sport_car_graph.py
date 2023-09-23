from sport_car_database import CarData


class GraphPlotter:
    def __init__(self):
        self.cd = CarData()
        self.x = None
        self.y = None

    def bar_plotter(self, ax):
        self.x, self.y = self.cd.bar_data()
        ax.bar(self.x, self.y, color="purple")
        ax.set_xlabel('Car Make')
        ax.set_xticklabels(self.x, rotation=45)
        ax.set_ylabel('Number of Car Models')
        ax.set_title('Number of Sport Cars in each Year')

    def pie_plotter(self, ax):
        self.x, self.y = self.cd.pie_data()
        ax.pie(self.y, labels=self.x, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('Proportion of the Number of Sport Cars')

    def histogram_plotter(self, ax):
        self.x = self.cd.histogram_data()
        ax.hist(self.x, bins=10, color="maroon")
        ax.set_xlabel('Car Make', fontsize=8)
        ax.set_xticklabels(self.x, rotation=40, fontsize=5)
        ax.set_ylabel('Frequency')
        ax.set_title('Distribution of Sport Car')

    def scatter_plotter(self, ax):
        self.x, self.y = self.cd.scatter_data()
        ax.scatter(self.x, self.y, color="darkblue")
        ax.set_xlabel('Horsepower')
        ax.set_ylabel('Torque')
        ax.set_title(
            'Relationship between Horsepower and Torque of Sport Cars')
