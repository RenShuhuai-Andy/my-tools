# reference: http://www.tensorinfinity.com/paper_198.html

# 全局变量，用于存储中间层的 feature
total_feat_out = []
total_feat_in = []
def hook_fn_forward(module, input, output):
    print(type(module).__name__)
    print('input', input)  
    print('output', output)
    total_feat_out.append(output)  # 然后分别存入全局 list 中
    total_feat_in.append(input)


total_grad_out = []
total_grad_in = []
def hook_fn_backward(module, grad_input, grad_output):
    print(module)  # 为了区分模块
    # 为了符合反向传播的顺序，我们先打印 grad_output
    print('grad_output', grad_output) 
    # 再打印 grad_input
    print('grad_input', grad_input)
    # 保存到全局变量
    total_grad_in.append(grad_input)
    total_grad_out.append(grad_output)


model = Model()
modules = model.named_children()
for name, module in modules:
    module.register_forward_hook(hook_fn_forward)
    module.register_backward_hook(hook_fn_backward)