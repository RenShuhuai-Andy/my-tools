# 服务器常用 shell 命令

## 查询相关信息

### CPU 查询

- 查看CPU使用情况（按1查看每个CPU逻辑核的使用率）：

`top`

- 查看CPU型号：

```
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
cat /proc/cpuinfo | grep physical | uniq -c
```

### GPU 查询

- 查看GPU使用情况： 

`nvidia-smi –l`

- 查看GPU型号：

`lspci | grep -i vga`

### 进程查询

- 查看 PID4761 对应的用户和进程：

`ps -aux|grep 4761`

- 查看 PID4761 对应的存活线程：

`pstree -p 4761`

`cat /proc/4761/status`

## CPU 设定

- 绑核，将 PID9865 的进程绑到0,2,5-11号CPU上：

`taskset -cp 0,2,5-11 9865`

## GPU 设定

- 指定GPU对象：

`os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2"`

- 设置定量的GPU使用量： 

``` 
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.9  # 占用GPU90%的显存
config.gpu_options.allow_growth = True  # 动态增减显存
session = tf.Session(config=config) 
```

- 若使用Keras：

```
from keras import backend as K
K.set_session(tf.Session(config=config))
```

## python 相关

- 指定pip源：

`pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple`

- 查看库的安装位置：

`pip show package_name`

- 命令行输入python语句：

`python -c 'import keras as k; print(k.__version__)'`

- 运行 python 程序，向控制台输出同时重定向到 out.txt：

`python -c "print('test')" | tee -a out.txt`

- 运行 python 程序并忽略 WARNING 输出;

`python -W ignore file.py`

- 虚拟环境相关操作：

```
conda create -n env_name python=3.6
source activate env_name
source deactivate
conda install -n env_name package_name
conda remove -n env_name --all
conda remove --name env_name package_name
```

## 文件操作

- 删除当前目录下的所有文件：

`rm -rf ./*`

- 修改当前整个文件夹的权限：

`chmod -R 777 ./`

## 修改环境变量

- 直接使用 export 命令：

```
export PATH=xxx
export https_proxy=xxx
```

- 修改 `/etc/profile`（对所有用户生效）：

`vi /etc/profile`

- 修改 `~/.bashrc`（对当前用户生效）：

`vi ~/.bashrc`

## Tensorboard

`tensorboard.exe --logdir=\path\to\logs`

## Docker

[只要一小时，零基础入门Docker - 笑虎的文章 - 知乎](https://zhuanlan.zhihu.com/p/23599229)

## tmux

[tmux：打造精致与实用并存的终端](https://segmentfault.com/a/1190000008188987)

[Tmux 快捷键 & 速查表 & 简明教程](https://gist.github.com/ryerh/14b7c24dfd623ef8edc7)

- 创建tmux会话：

`tmux new-session -s <会话名称>`