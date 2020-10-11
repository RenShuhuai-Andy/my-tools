import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
import numpy as np


def softmax(x):
    '''Compute softmax values for each sets of scores in x.'''
    e_x = np.exp(x - np.max(x, axis=1)[:, np.newaxis])
    return e_x / e_x.sum(axis=1)


def plot_attention_headmap(data, columns, index, figname='attn.png', tick_spacing=1):
    df = pd.DataFrame(data, columns=columns, index=index)

    fig = plt.figure()

    ax = fig.add_subplot(111)

    cax = ax.matshow(df, interpolation='nearest', cmap='Blues')
    fig.colorbar(cax)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    ax.set_xticklabels([''] + list(df.columns))
    ax.set_yticklabels([''] + list(df.index))
    # plt.savefig(figname)
    plt.show()


if __name__ == '__main__':
    data = np.array([[5, 2, 1],
                     [4, 6, 3],
                     [2, 4, 5]])
    data = softmax(data)
    plot_attention_headmap(data, ['%d' % i for i in range(data.shape[1])], ['%d' % i for i in range(data.shape[0])])
    # for pytorch
    # plot_attention_headmap(data, ['%d' % i for i in range(data.size(1))], ['%d' % i for i in range(data.size(0))])
