import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# set style
sns.set(style='whitegrid')



if __name__ == '__main__':
    data = pd.read_csv('logs.csv', skipinitialspace=True)

    # get datasets
    datasets = set(data['dataset'])
    for dataset in datasets:
        subdata = data[data['dataset'] == dataset]


    print(data)
    sns.violinplot(x='enc', y='micro', hue='dataset', data=data)
    plt.show()