import math
import random
import numpy as np

def get_batch_data(inputs, batch_size=None, shuffle=False):
    rows = len(inputs)
    indices = list(range(rows))
    if shuffle:
        random.seed(100)
        random.shuffle(indices)
    i = 0  # TODO better solution?
    while i <= math.ceil(rows / batch_size): 
        batch_indices = np.asarray(indices[0:batch_size])  # 产生一个batch的index
        indices = indices[batch_size:] + indices[:batch_size]  # 循环移位，以便产生下一个batch

        data = np.asarray(inputs)
        batch_data = data[batch_indices].tolist()  # 使用下标查找，必须是ndarray类型类型
        i += 1
        yield batch_data

inputs = 
batch_size = 
batches = get_batch_data(inputs, batch_size=batch_size)

for batch in batches:
    