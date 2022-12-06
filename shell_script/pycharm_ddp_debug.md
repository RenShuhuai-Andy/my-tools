# PyCharm 调试 torch.distributed.launch

### 一、远程服务器端

使用软链接将 anaconda 环境中，torch 包里的 launch.py 关联到项目目录下
 
```bash
ln -s /home/ubuntu/anaconda3/envs/${env-name}/lib/python3.8/site-packages/torch/distributed/launch.py /path/to/your/program
```

随后将远程服务器项目目录下的 launch.py 下载到本地项目目录中，使服务器和本地的两个 launch.py 直接关联


### 二、本地配置

假设原始的训练命令为：
```bash
python3 -m torch.distributed.launch --nproc_per_node=1 --master_port=1234 train.py --other_parameters
```

则使用 pycharm 调试时需要：

点击 `Edit Configurations` 进入参数配置界面，配置 `Script path` 为本地 launch.py 的路径；在 `Parameters` 里添加 `--nproc_per_node=1 --master_port=1234 train.py --other_parameters`

### Reference：

- [Pycharm 调试debug torch.distributed.launch](https://blog.csdn.net/liu_yuan_kai/article/details/118706387)
- [如何在pycharm中运行/调试torch分布式训练 - purity缔造者的文章 - 知乎](https://zhuanlan.zhihu.com/p/144815822)