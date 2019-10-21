import pandas as pd
import matplotlib.pyplot as plt # requires matplotlib 3.1.1
import numpy as np

df_all = pd.DataFrame({'var': ['bid', 'on', 'off', 'bid', 'on', 'off'],
                   'aud': ['H', 'H', 'H', 'L', 'L', 'L'],
                   'eff': [0.1, 0.2, 0.3, 0.01, 0.02, 0.03],
                   'spend': [10313, 21240, 31240, 1, 2, 3],
                   'marg': [0.001, 0.002, 0.003, 0.0001, 0.0002, 0.0003],
                   'colours': ['#185177', '#FAA22C', '#8FC5E8', '#185177', '#FAA22C', '#8FC5E8']})

df = df_all[df_all.aud=='H'].reset_index(drop=True)

def _create_bubble_plots(df, x, y, size, colours, labels, title):

    x='eff'
    y='marg'
    size='spend'
    colours = 'colours'
    labels = 'var'
    title = 'H'

    x_plot = df[x]
    y_plot = df[y]
    size_plot = df[size]
    colours_plot = df[colours]
    labels_plot = df[labels]

    g, ax = plt.subplots()
    scatter = ax.scatter(x_plot, y_plot, c=[colours_plot[i] for i in range(len(x_plot))],
                         s=(np.round(size_plot) // 10000) * 100)
    # create legend for colors
    handles = [plt.Line2D([], [], ls="", marker="o", color=c) for c in colours_plot]
    legend1 = ax.legend(handles, labels_plot, loc=(1.04,0.5), title="var")

    ax.add_artist(legend1)
    # create legend for sizes
    handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
    ax.legend(handles, labels, loc=(1.04,0), title="Spend in 100000 $")
    # adjust axes' range and labels
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xlim(0, x_plot.max()*1.1)
    plt.ylim(0, y_plot.max()*1.1)

    plt.title(title)

    plt.savefig('bubbles.png', bbox_inches='tight')
