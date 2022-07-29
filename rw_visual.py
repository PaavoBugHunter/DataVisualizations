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
    coordinate_points = range(my_walker.num_points)
    ax.scatter(my_walker.x_coordinate, my_walker.y_coordinate, s=15)
    #c = coordinate_points, cmap = plt.cm.Blues,
    ax.scatter(my_walker.x_coordinate[0], my_walker.y_coordinate[0], c = "red", s = 100)
    ax.scatter(my_walker.x_coordinate[-1], my_walker.y_coordinate[-1], c = "green", s = 100)
    ax.axis([min(my_walker.x_coordinate) - 20, max(my_walker.x_coordinate) + 20, min(my_walker.y_coordinate) - 20, max(my_walker.y_coordinate) + 20])
    ax.set_title("Random walk illustration with 5000 steps")
    ax.set_xlabel("X-coordinate")
    ax.set_ylabel("Y-coordinate")
    
    plt.show()

    #Ask for repeat
    another_round = input("Another one (y/n)?")
    if another_round == "n":
        break