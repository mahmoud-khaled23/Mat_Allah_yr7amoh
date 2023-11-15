
import numpy as np
import matplotlib.pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]


def bar_plot():
    x_indexes = np.arange(len(ages_x))
    width = 0.25

    # i can use np_ages_x instead of x_indexes and xticks
    # np_ages_x = np.array(ages_x)

    plt.bar(x_indexes - width, dev_y, width=width, label='All Developers')

    plt.bar(x_indexes, py_dev_y, width=width, label="python")

    plt.bar(x_indexes + width, js_dev_y, width=width, label="JavaScript")

    # legend() : describe elements in the graph
    plt.legend()
    plt.xticks(ticks=x_indexes, labels=ages_x)
    plt.title("my bar chart")
    plt.xlabel("Age")
    plt.ylabel("Salary")
    plt.show()


if __name__ == '__main__':
    bar_plot()

    print("hello, im there")
