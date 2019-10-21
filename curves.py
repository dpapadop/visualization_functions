import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.ticker as mtick

pd.set_option('max_columns', 50)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 175)




data_tmp = pd.DataFrame({'x': [0, 14, 28, 42, 56, 0, 14, 28, 42, 56],
                         'y': [0, 0.003, 0.006, 0.008, 0.001, 0 * 2, 0.003 * 2, 0.006 * 2, 0.008 * 2, 0.001 * 2],
                         'cat': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
                         'color': ['#B5D8F0', '#B5D8F0', '#B5D8F0', '#B5D8F0', '#B5D8F0', '#247AB2',
                                   '#247AB2', '#247AB2', '#247AB2', '#247AB2'],
                         'point': [14, 14, 14, 14, 14, 28, 28, 28, 28, 28],
                         'linestyles': ['-', '-', '-', '-', '-', '--', '--', '--', '--', '--']})

def get_dash_pattern(style):
    _, dash = mpl.lines._get_dash_pattern(style)
    return dash if dash else (None, None)
    

palette = dict(zip(data_tmp.cat, data_tmp.color))
dashes = dict(zip(data_tmp.cat, data_tmp.linestyles))
dashes = {k: get_dash_pattern(v) for k, v in dashes.items()}

ax = sns.lineplot(x="x", y="y", hue="cat", data=data_tmp, palette=palette, style='cat',  dashes=dashes)
ax = sns.scatterplot(x="point", y="y", hue="cat", data=data_tmp[data_tmp.point == data_tmp.x], palette=palette,
                     legend=False)

ax.set_title('title')
ax.set_ylabel('y label')
ax.set_xlabel('x label')
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.xaxis.set_major_formatter(tick)
ax.set_xticks(np.arange(0, data_tmp.x.max(), data_tmp.x.max()/4))
ax.legend(loc=(1.04, 0))
plt.show()
