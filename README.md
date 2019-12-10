# My Tools

常用的一些轮子



## shell script

- [install_package.sh](/shell_script/install_package.sh)：使用 conda 命令根据 requirement.txt 安装包。

- [common_commands.md](/shell_script/common_commands.md)：服务器常用命令。

## python script

#### visualizetion

- [t_SNE.py](/python_script/visualization/t_SNE.py)：使用 t_SNE 进行降维并可视化。

#### printer

- [logger.py](/python_script/printer/logger.py)：使用 logging 模块同时将日志打印到终端和文件。

#### cuda_memory_tracker

参考：https://github.com/Oldpan/Pytorch-Memory-Utils

- [model_size_estimate.py](/python_script/cuda_memory_tracker/model_size_estimate.py)：估计 pytorch 模型参数和中间变量所占显存的大小。
- [gpu_mem_track.py](/python_script/cuda_memory_tracker/gpu_mem_track.py)：精确跟踪 pytorch 模型的显存使用情况（需要安装 NVIDIA 的 python 环境库 pynvml：`pip install nvidia-ml-py3`）。
- [examples.py](/python_script/cuda_memory_tracker/examples.py)：对于 `gpu_mem_track.py` 的使用示例。

[hook.py](/python_script/hook.py)：使用 pytorch hook 获取中间层变量的值和梯度。

[get_batch.py](/python_script/get_batch.py)：获取一个 batch_siez 的 data。