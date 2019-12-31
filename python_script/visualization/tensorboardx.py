# reference: https://zhuanlan.zhihu.com/p/36946874
# https://zhuanlan.zhihu.com/p/37022051
# https://pytorch.apachecn.org/docs/1.2/intermediate/tensorboard_tutorial.html
from tensorboardX import SummaryWriter
writer = SummaryWriter('./log')

total_steps = epoch * len(train_loader) + i

# draw scalar(s)
# single line
writer.add_scalar('loss', loss, total_steps)
# multi lines in one figure
writer.add_scalars('losses', {'loss_1': loss_1, 'loss_2': loss_2}, total_steps)

# draw histogram
for pi, (name, param) in enumerate(model.named_parameters()):
    writer.add_histogram(name, param, 0)

writer.close()