import numpy as np
import matplotlib.pyplot as plt

def plot_pie():
    slices = [30, 60, 10, 40]
    labels = ['ahmed', 'mohamed', 'koko', 'others']
    colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

    plt.pie(slices, labels=labels, colors=colors)
    plt.title("my Pie Chart")
    plt.tight_layout()
    plt.show()
    # Median Developer Salaries by Age
    pass

def plot_langs():
    slices = [59219, 55466, 47544, 36443, 35917]
    labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

    # explode: how much the piece is far from circle radius
    explode = [0, 0, 0, 0.1, 0]

    plt.pie(slices, labels=labels, explode=explode,
            # startangle=90,
            shadow=True, autopct='%1.1f%%')
    plt.title("my Pie Chart")
    plt.tight_layout()
    plt.show()

# colors in hexa:
# blue: #008fd5
# red: #fc4f30
# yellow: #e5ae37
# green: #6d904f


if __name__ == '__main__':

    plot_langs()


"""

# code snippet
# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

"""

