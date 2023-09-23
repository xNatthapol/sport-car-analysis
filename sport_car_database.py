import pandas as pd


class CarData:
    def __init__(self):
        self.__df_data = pd.read_csv('sport_car_data.csv')

    @property
    def data(self):
        return self.__df_data

    def get_mean(self, column_name):
        return format(self.__df_data[column_name].mean(), '.2f')

    def get_median(self, column_name):
        return format(self.__df_data[column_name].median(), '.2f')

    def get_mode(self, column_name):
        return self.__df_data[column_name].mode().values[0]

    def get_std(self, column_name):
        return format(self.__df_data[column_name].std(), '.2f')

    def get_max(self, column_name):
        return self.__df_data[column_name].max()

    def get_min(self, column_name):
        return self.__df_data[column_name].min()

    def bar_data(self):
        car_make_year = self.__df_data['Year'].value_counts().sort_index()
        year_str = list(map(str, car_make_year.index.tolist()))
        return year_str, car_make_year.values.tolist()

    def pie_data(self):
        other_count = 0
        new_car_make_name = []
        new_car_make_count = []
        car_make = self.__df_data['Car Make'].value_counts()
        car_make_name = car_make.index.tolist()
        car_make_count = car_make.values.tolist()
        for i in range(len(car_make_count)):
            if car_make_count[i] < 13:
                other_count += car_make_count[i]
            else:
                new_car_make_name.append(car_make_name[i])
                new_car_make_count.append(car_make_count[i])
        new_car_make_name.append('Others')
        new_car_make_count.append(other_count)
        return new_car_make_name, new_car_make_count

    def histogram_data(self):
        return self.__df_data['Car Make']

    def scatter_data(self):
        return self.__df_data['Horsepower'].values.tolist(), self.__df_data[
            'Torque'].values.tolist()
