# My Tools

常用的一些轮子



## shell script

- [install_package.sh](/shell_script/install_package.sh)：使用 conda 命令根据 requirement.txt 安装包。

- [common_commands.md](/shell_script/common_commands.md)：服务器常用命令。

## python script

#### visualizetion

- [t_SNE.py](/python_script/visualization/t_SNE.py)：使用 t_SNE 进行降维并可视化。
- [tensorboardx.py](/python_script/visualization/tensorboardx.py)：使用 tensorboardX 对训练进行可视化。
- [matplotlib.py](/python_script/visualization/matplotlib.py)：使用 matplotlib 画折线图的一个实例，包含多条折线时的配色方案。
  - matplotlib 画图参考 [matplotlib：先搞明白plt. /ax./ fig再画 - 姚太多啊的文章 - 知乎](https://zhuanlan.zhihu.com/p/93423829)

#### printer

- [logger.py](/python_script/printer/logger.py)：使用 logging 模块同时将日志打印到终端和文件。

#### cuda_memory_tracker

参考：https://github.com/Oldpan/Pytorch-Memory-Utils

- [model_size_estimate.py](/python_script/cuda_memory_tracker/model_size_estimate.py)：估计 pytorch 模型参数和中间变量所占显存的大小。

- [gpu_mem_track.py](/python_script/cuda_memory_tracker/gpu_mem_track.py)：精确跟踪 pytorch 模型的显存使用情况（需要安装 NVIDIA 的 python 环境库 pynvml：`pip install nvidia-ml-py3`）。

- [examples.py](/python_script/cuda_memory_tracker/examples.py)：对于 `gpu_mem_track.py` 的使用示例。

#### configargparse

统一了命令行参数、配置文件、环境变量等设置，并创建为单例模式，使得它们在代码的任何地方都可以通过 `Config.get_instatnce()` 被导入和使用。

- [example.py](/python_script/configargparse/example.py)：使用 configargparse 的案例。
- [model.yaml](/python_script/configargparse/model.yaml)：yaml 风格的配置文件案例。

#### other

- [hook.py](/python_script/hook.py)：使用 pytorch hook 获取中间层变量的值和梯度。

- [get_batch.py](/python_script/get_batch.py)：获取一个 batch_siez 的 data。

- [time.py](/python_script/time.py)：计算程序运行时间。

## v2ray script

- [README.md](/v2ray_script/README.md)：v2ray的相关命令、配置、阅读材料。