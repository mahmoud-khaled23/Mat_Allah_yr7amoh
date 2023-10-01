import numpy as np
import matplotlib.pyplot as plt

def salaries_plot():
    # Median Developer Salaries by Age
    ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    dev_y = [38496, 42000, 46752, 49320, 53200,
             56000, 62316, 64928, 67317, 68748, 73752]

    # Median Python Developer Salaries by Age
    py_dev_y = [45372, 48876, 53850, 57287, 63016,
                65998, 70003, 70000, 71496, 75370, 83640]

    # plt.style.use('ggplot')
    # plt.xkcd()
    plt.title('Median Salary by Age (USD)')
    plt.plot(ages_x, dev_y, '--y', marker='o', linewidth='4', label='All Devs')
    plt.plot(ages_x, py_dev_y, color='b', linestyle=':', label='Py Devs')
    plt.legend() # Labels are sent at the same line with the data
    plt.grid(True)
    # plt.savefig('plooto.png')
    # plt.tight_layout()
    plt.show()




if __name__ == '__main__':

    salaries_plot()

    print("klo ta7t elcontrol")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
