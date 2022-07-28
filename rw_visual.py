import matplotlib.pyplot as plt

#How to get Python 3.10.4 compatible virtual environment? Done

from random_walk import RWalkGenerator

while True:
    #Make a random walk
    my_walker = RWalkGenerator()


    my_walker.fill_walk()

    #Plot the points in the walk
    plt.style.use("fivethirtyeight")
    fig, ax = plt.subplots()
    ax.scatter(my_walker.x_coordinate, my_walker.y_coordinate, s=15)
    plt.show()

    #Ask for repeat
    another_round = input("Another one (y/n)?")
    if another_round == "n":
        break