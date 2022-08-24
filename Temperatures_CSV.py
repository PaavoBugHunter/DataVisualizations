import csv

import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots()

from datetime import datetime

'''Prgram for displaying temperatures from data stored in a csv-file.'''
filename = "sitka_temperature.csv" #File name must include path to data-file's location

class Excavator():
    def __init__(self):
        '''No particular attributes needed'''

    def print_header(self):
        '''Prints csv-file's header'''
        with open(filename) as data_source:
            data_reader = csv.reader(data_source)
            header_row = next(data_reader)
        for index, title in enumerate(header_row):
            print(index, title)
            #print(header_row)

    def print_toptemps(self):
        '''Prints the high-temperature of every recorded day'''
        toptemps, lowtemps, dates = [], [], []
        with open(filename) as data_source:
            data_reader = csv.reader(data_source)
            for row in data_reader:
                if row[5] == "TMAX":
                    pass
                else:
                    toptemps.append(int(row[5]))
                    lowtemps.append(int(row[6]))
                    obs_date = datetime.strptime(row[2], "%Y-%m-%d")
                    dates.append(obs_date)

        print(toptemps)
        #print(dates)

        ax.plot(dates, toptemps, c = "red")
        ax.plot(dates, lowtemps, c = "blue")
        plt.title("Daily top temperatures, July 2018", fontsize = 24)
        plt.xlabel("", fontsize = 16)
        fig.autofmt_xdate()
        plt.ylabel("Temp.", fontsize = 16)
        plt.tick_params(axis="both", which="major", labelsize=16)
        plt.show()


my_excavator = Excavator()
my_excavator.print_header()
my_excavator.print_toptemps()
