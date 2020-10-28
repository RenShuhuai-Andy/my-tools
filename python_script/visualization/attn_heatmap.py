import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
import numpy as np


def softmax(x):
    '''Compute softmax values for each sets of scores in x.'''
    e_x = np.exp(x - np.max(x, axis=1)[:, np.newaxis])
    return e_x / e_x.sum(axis=1)


def plot_attention_heatmap(data, columns, index, figname='attn.png', tick_spacing=1):
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


def plot_attention_heatmap_for_multimodal(data, columns, index, figname='attn.png'):
    '''
    use picture as tick labels: https://stackoverflow.com/questions/44246650/automating-bar-charts-plotting-to-show-country-flags-as-ticklabels
    data: attention map tensor
    columns / index: list of token or images_to_plot (which is a dict like {regions, example_id}, where regions is
                        a list of ndarray which is cropped from an image loaded by plt.imread)
    '''

    def _annotation_boxes(images_to_plot, boxes_type, xybox, ax):
        regions = images_to_plot['regions']
        image_boxes = []
        for i, region in enumerate(regions):
            image_box = OffsetImage(region, zoom=0.2)
            image_box.image.ax = ax
            # OffsetImage is a sub-class of Artist, and has get_tight_box method, while AnnotationBbox is not.
            # see https://matplotlib.org/3.3.2/api/artist_api.html
            image_boxes.append(image_box)
            if boxes_type == 'columns':
                xy = (0, i)
            elif boxes_type == 'index':
                xy = (i, 0)
            else:
                raise ValueError()
            ab = AnnotationBbox(image_box, xy, xybox=xybox, frameon=False,
                                xycoords='data', boxcoords="offset points", pad=0)
            ax.add_artist(ab)

    df = pd.DataFrame(data, columns=['%d' % d for d in range(data.shape[1])],
                      index=['%d' % d for d in range(data.shape[0])])

    fig = plt.figure(figsize=(14, 12))
    ax = fig.add_subplot(111)
    cax = ax.matshow(df, interpolation='nearest', cmap='hot_r')
    fig.colorbar(cax)

    tick_spacing = 1
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    image_boxes = []
    if type(columns) == dict and type(index) == dict:
        image_id = columns['image_id']
        ax.set_title(image_id)
        image_boxes += _annotation_boxes(columns, 'columns', (-100, 0), ax)
        image_boxes += _annotation_boxes(index, 'index', (0, 100), ax)
    elif type(columns) == dict:
        image_id = columns['image_id']
        ax.set_title(image_id)
        image_boxes += _annotation_boxes(columns, 'columns', (-100, 0), ax)
        plt.xticks(rotation=45)
        ax.set_xticklabels([''] + index)
    elif type(index) == dict:
        image_id = index['image_id']
        ax.set_title(image_id)
        image_boxes += _annotation_boxes(index, 'index', (0, 100), ax)
        ax.set_yticklabels([''] + columns)
    else:
        plt.xticks(rotation=45)
        ax.set_xticklabels([''] + columns)
        ax.set_yticklabels([''] + index)
        image_boxes = None

    plt.savefig(figname, bbox_extra_artists=image_boxes, bbox_inches='tight')


if __name__ == '__main__':
    data = np.array([[5, 2, 1],
                     [4, 6, 3],
                     [2, 4, 5]])
    data = softmax(data)
    plot_attention_heatmap(data, ['%d' % i for i in range(data.shape[1])], ['%d' % i for i in range(data.shape[0])])
    # for pytorch
    # plot_attention_heatmap(data, ['%d' % i for i in range(data.size(1))], ['%d' % i for i in range(data.size(0))])
