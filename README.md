# My Tools

常用的一些轮子



## shell script

- [common_commands.md](/shell_script/common_commands.md)：服务器常用命令。
- [install_package.sh](/shell_script/install_package.sh)：使用 conda 命令根据 requirement.txt 安装包。
- [pycharm_ssh.md](/shell_script/pycharm_ssh.md)：有跳板机的情况下通过 pycharm 连接远程服务器。
- [pycharm_ddp_debug.md](/shell_script/pycharm_ddp_debug.md)：使用 pycharm 对 pytorch ddp 进行 debug。

## python script

<details>
<summary>visualization</summary>

##### 训练可视化

- [wandb for pytorch](https://docs.wandb.ai/guides/integrations/pytorch)：使用 wandb 对训练进行可视化。
- [tensorboardx.py](/python_script/visualization/tensorboardx.py)：使用 tensorboardX 对训练进行可视化。

##### 结果可视化

- [plt_vis.ipynb](/python_script/visualization/plt_vis.ipynb)：使用 matplotlib 进行可视化的示例，包括：
    - [官方 colormap](https://matplotlib.org/tutorials/colors/colormaps.html)、 [配色方案](https://colorhunt.co/palettes/popular)、 [plt style](https://matplotlib.org/3.1.1/gallery/style_sheets/style_sheets_reference.html)
    - 折线图
    - 双栏折线图
    - 直方图
    - (多模态的) attention matrix 热力图
    - 使用 t_SNE 进行降维的可视图
    - 雷达图 ([acknowledge](https://github.com/muzairkhattak/multimodal-prompt-learning/issues/5))
    - 伪蜡烛图
    - 拟合散点图并画出趋势线
    - 多条折线图
    - 太阳图
    - 单位球面
- matplotlib 画图参考 [matplotlib：先搞明白plt. /ax./ fig再画 - 姚太多啊的文章 - 知乎](https://zhuanlan.zhihu.com/p/93423829)
- [The Python Graph Gallery](https://www.python-graph-gallery.com/)：使用 python 绘制各种类型的图表
- UMAP:
    - [Understanding UMAP](https://pair-code.github.io/understanding-umap/)
    - [[译] 理解 UMAP(2): UMAP和一些误解 - 邻泽居士的文章 - 知乎](https://zhuanlan.zhihu.com/p/352461768)
- [bertviz](https://github.com/jessevig/bertviz)：对 huggingface transformer attention/model/neuron 的可视化
- [Transformer-Explainability](https://github.com/hila-chefer/Transformer-Explainability)：可视化 transformer 注意力在输入上的分配
- [Gradio](https://github.com/gradio-app/gradio)：为机器学习模型、API或函数创建GUI
- [Terminalizer](https://terminalizer.com/)：为命令行演示创建gif
</details>

<details>
<summary>pytorch</summary>

- [[深度学习框架] PyTorch常用代码段 - Jack Stark的文章 - 知乎](https://zhuanlan.zhihu.com/p/104019160)
- [PyTorch Cookbook（常用代码段整理合集） - 张皓的文章 - 知乎](https://zhuanlan.zhihu.com/p/59205847)
- [Bert Inner Workings - George Mihaila](https://colab.research.google.com/github/gmihaila/ml_things/blob/master/notebooks/pytorch/bert_inner_workings.ipynb)：A tutorial notebook for understanding the inner workings of Bert.
</details>

<details>
<summary>printer</summary>

- [logger.py](/python_script/printer/logger.py)：使用 logging 模块同时将日志打印到终端和文件。
</details>

<details>
<summary>cuda_memory_tracker</summary>

参考：https://github.com/Oldpan/Pytorch-Memory-Utils

- [model_size_estimate.py](/python_script/cuda_memory_tracker/model_size_estimate.py)：估计 pytorch 模型参数和中间变量所占显存的大小。
- [gpu_mem_track.py](/python_script/cuda_memory_tracker/gpu_mem_track.py)：精确跟踪 pytorch 模型的显存使用情况（需要安装 NVIDIA 的 python 环境库 pynvml：`pip install nvidia-ml-py3`，或 `conda install -c conda-forge pynvml`）。
- [examples.py](/python_script/cuda_memory_tracker/examples.py)：对于 `gpu_mem_track.py` 的使用示例。

另一种监控显存的方法：[Pytorch Profiler](https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)

[PyTorch显存机制分析 - Connolly的文章 - 知乎](https://zhuanlan.zhihu.com/p/424512257)
</details>

<details>
<summary>configargparse</summary>

统一了命令行参数、配置文件、环境变量等设置，并创建为单例模式，使得它们在代码的任何地方都可以通过 `Config.get_instatnce()` 被导入和使用。

- [example.py](/python_script/configargparse/example.py)：使用 configargparse 的案例。
- [model.yaml](/python_script/configargparse/model.yaml)：yaml 风格的配置文件案例。

另一种指定实验配置的方法：[Sacred](https://github.com/IDSIA/sacred)
</details>

<details>
<summary>other</summary>

- [hook.py](/python_script/hook.py)：使用 pytorch hook 获取中间层变量的值和梯度。
- [get_batch.py](/python_script/get_batch.py)：获取一个 batch_siez 的 data。
- [time.py](/python_script/time.py)：计算程序运行时间。
- [model_stats.py](/python_script/model_stats.py)：打印模型状态，包括参数名、参数量、显存开销、Flops、激活张量的大小等。
- [multi_process.py](/python_script/multi_process.py)：多进程的使用示例。
- [gpus.py](/python_script/gpus.py): 空占GPU资源的脚本
- [tax_calculator.py](/python_script/tax_calculator.py): 按自然年计算个税
</details>

## latex

- [def_and_cmd.tex](/latex/def_and_cmd.tex)：latex中常用的包、定义、命令等。

## v2ray script

- [README.md](/v2ray_script/README.md)：v2ray的相关命令、配置、阅读材料。