import matplotlib.pyplot as plt
from sklearn import manifold

def t_sne(x, y, figure_name):
    '''
    x is a datamat, type is ndarray, shape(x)[0] reps the number of data, shape(x)[1] reps the ori dim of a data
    y is labels, type is array, shape(y)[0] reps the number of labels of data.
    '''
    tsne = manifold.TSNE(n_components=2, init='pca', random_state=501)
    x_tsne = tsne.fit_transform(x)
    print("Org data dimension is {}. Embedded data dimension is {}".format(x.shape[-1], x_tsne.shape[-1]))

    x_min, x_max = x_tsne.min(0), x_tsne.max(0)
    x_norm = (x_tsne - x_min) / (x_max - x_min)  # normalization
    plt.figure(figsize=(8, 8))
    for i in range(x_norm.shape[0]):
        plt.text(x_norm[i, 0], x_norm[i, 1], str(y[i]), color=plt.cm.Set1(y[i]),
                 fontdict={'weight': 'bold', 'size': 9})
    plt.title(figure_name)
    plt.xticks([])
    plt.yticks([])
    plt.show()