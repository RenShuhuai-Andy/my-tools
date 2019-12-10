# reference: https://oldpan.me/archives/how-to-use-memory-pytorch
# hint: without test
import numpy as np
import torch

def model_size(model, input, type_size=4):
    '''
    calculate model size
    :para model: a pytorch model
    :para input: input of the model
    :para type_size: assume the data type is 32-bit floating point, so the type_size is 4, which means 4B
    '''
    # cal size of weight parameters, units is B
    para = sum([np.prod(list(p.size())) for p in model.parameters()])
    print('Model {} : params: {:4f}M'.format(model._get_name(), para * type_size / 1000 / 1000))

    # cal size of middle parameters of the model
    input_ = input.clone()
    input_.requires_grad_(requires_grad=False)

    mods = list(model.modules())
    out_sizes = []

    for i in range(1, len(mods)):  # TODO ugly
        m = mods[i]
        if isinstance(m, torch.nn.ReLU):
            if m.inplace:  # no need to cal is Relu function is inplace
                continue
        out = m(input_)
        out_sizes.append(np.array(out.size()))
        input_ = out

    total_nums = 0
    for i in range(len(out_sizes)):
        s = out_sizes[i]
        nums = np.prod(np.array(s))
        total_nums += nums

    print('Model {} : intermedite variables: {:3f} M (without backward)'
          .format(model._get_name(), total_nums * type_size / 1000 / 1000))
    print('Model {} : intermedite variables: {:3f} M (with backward)'
          .format(model._get_name(), total_nums * type_size*2 / 1000 / 1000))
