import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plt.tight_layout() -- automatic paddings

if __name__ == '__main__':
    plt.style.use('seaborn')
    #
    # x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
    # y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
    #
    # colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

    data = pd.read_csv('data/2019-05-31-data.csv')

    view_count = data['view_count']
    likes = data['likes']
    ratio = data['ratio']

    plt.scatter(view_count, likes, c=ratio, cmap='Reds',
                edgecolors='black', alpha=.9)

    cbar = plt.colorbar()
    cbar.set_label('like/dislike ratio')

    plt.xscale('log')
    plt.yscale('log')

    plt.title('youtube trending videos')
    plt.xlabel('view count')
    plt.ylabel('likes')
    # cbar = plt.colorbar()
    # cbar.set_label("duration")
    plt.show()

    print("Scatter Plot")
