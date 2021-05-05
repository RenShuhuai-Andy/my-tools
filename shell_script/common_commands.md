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

- 查看GPU使用情况/驱动版本/CUDA版本： 

`nvidia-smi –l`

- 寻找GPU利用率瓶颈 ([参考](https://zhuanlan.zhihu.com/p/53345706))：

`watch -n 0.1 nvidia-smi`

- 查看GPU型号：

`lspci | grep -i vga`

- 查看cuda版本：

```
cat /usr/local/cuda/version.txt
nvcc --version
```

### DL框架与兼容性查询

- 查看torch版本和torch cuda版本：

`python -c "import torch; print('torch version: ', torch.__version__); print('cuda version: ', torch.version.cuda)"`

- [显卡,显卡驱动,nvcc,cuda driver,cudatoolkit,cudnn到底是什么？ - marsggbo的文章 - 知乎](https://zhuanlan.zhihu.com/p/91334380)
- [CUDA与nvidia driver版本兼容性检查表](https://github.com/NVIDIA/nvidia-docker/wiki/CUDA)
- [CUDA与pytorch版本兼容性检查表](https://pytorch.org/get-started/previous-versions/)
- [CUDA与TensorFlow版本兼容性检查表](https://www.tensorflow.org/install/source#tested_build_configurations)
- [TensorFlow与keras版本兼容性检查表](https://docs.floydhub.com/guides/environments/)
- [pytorch分布式训练环境检查](https://github.com/pytorch/pytorch/tree/master/test/distributed)
- [tensorflow1.x与2.x函数对照表 (不全)](https://docs.google.com/spreadsheets/d/1FLFJLzg7WNP6JHODX5q8BDgptKafq_slHpnHVbJIteQ/edit#gid=0)

- [Linux服务器中非 root 用户安装 (多版本) CUDA 和 cuDNN](https://www.jianshu.com/p/c95c5b6a4707)

### 内存查询

`free`

### 文件（夹）大小查询

- 查看当前文件夹大小：

`du -sh`

- 查看当前目录下所有文件夹的大小（参数--max-depth 表示深入目录的层数）：

` du -h --max-depth 1`

- 查看某个文件（夹）大小查询：

`du -h file/folder`

### 文件字节数/字数/行数查询

```
wc -lcw file1 [file2]
# -c: 统计字节数; -l: 统计行数; -w: 统计字数
```

### 进程查询

- 查看 PID4761 对应的用户和进程：

`ps -aux|grep 4761`

- 查看 PID4761 对应的存活线程：

`pstree -p 4761`

`cat /proc/4761/status`

- 查看某个用户的所有进程：

`top -U user_name`

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

```
# 临时指定
pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install scrapy -i https://pypi.doubanio.com/simple
# 永久指定
mkdir ~/.pip
vi ~/.pip/pip.conf
[global]
trusted-host=mirrors.aliyun.com
index-url=http://mirrors.aliyun.com/pypi/simple/
```

- 指定conda源：

```
conda config --add channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/'
conda config --add channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/'
conda config --set show_channel_urls yes

# 验证源
conda config --show channels
```

- 查看库的安装位置：

`pip show package_name`

- 命令行输入python语句：

`python -c 'import keras as k; print(k.__version__)'`

- 运行 python 程序，向控制台输出同时重定向到 out.txt：

`python -c "print('test')" | tee -a out.txt`

- 运行 python 程序并忽略 WARNING 输出：

`python -W ignore file.py`

- 虚拟环境相关操作：

```
# 可以使用 conda 时：
conda create -n env_name -y python=3.6
source activate env_name
source deactivate
conda install -n env_name -y package_name
conda remove -n env_name --all
conda remove --name env_name package_name
conda info --env
# 无法使用 conda 连网时：
python3 -m venv env_name
source env_name/bin/activate
deactivate
```

- 输出本地包环境到终端和文件：

`pip freeze | tee requirements.txt`

可以用 `pip freeze | grep tensor` 来显示仅含 `tensor` 的包名

- 命令行 pdb 调试：

```
python -m pdb xxx.py
(Pdb) b 8      # 设置断点。断点设置该文件的第8行（b即break的首字母）
(Pdb) b        # 显示所有断点。b命令，没有参数
(Pdb) cl 2     # 删除断点。删除第2个断点（clear的首字母）

(Pdb) n        # Step Over。单步执行（next的首字母）
(Pdb) s        # Step Into（step的首字母）
(Pdb) r        # Setp Return（return的首字母）
(Pdb) c        # Resume（continue的首字母）
(Pdb) j 10     # Run to Line。运行到地10行（jump的首字母）

(Pdb) p param  # 查看当前param变量值
(Pdb) l        # 查看运行到某处代码
(Pdb) a        # 查看全部栈内变量

(Pdb) h        # 帮助（help的首字母）
(Pdb) q        # 退出（quit的首字母）
```

- 开启http服务器

`python -m http.server`

## 文件操作

- 删除当前目录下的所有文件：

`rm -rf ./*`

- 修改当前整个文件夹的权限：

`chmod -R 777 ./`

- 打印当前路径：

`pwd`

- 文件拷贝

```
cp file1 file2     # 将文件file1复制成file2，复制后名称被改file2
cp file1 dir1      # 将文件file1复制到dir1目录下，复制后名称仍未file1
cp -r dir1 dir2    # 将目录dir1复制到dir2目录下，复制结果目录被改名为dir2
cp -r dir1/* dir2  # 将目录dir1下所有文件包括文件夹，都复制到dir2目录下
```

- 查看文件的访问时间和修改时间：

`stat file`

- 使用 `scp` 命令进行上传下载：

```
# 从服务器上下载文件
scp username@servername:/path/filename /Users/mac/Desktop（本地目录）
#上传本地文件到服务器
scp /path/filename username@servername:/path
# 从服务器下载整个目录 
scp -r username@servername:/root/（远程目录） /Users/mac/Desktop（本地目录）
# 上传目录到服务器
scp -r local_dir username@servername:remote_dir
# 注意:目标服务器要开启写入权限
# 把当前机器上的work文件夹拷贝到192.168.0.11机器的/home/work目录下
scp -r -P port /home/work/ user_name@192.168.0.11:/home/work/  
```

- 使用 `wget` 命令下载 Google drive 文件：

```
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=FILEID' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=FILEID" -O FILENAME && rm -rf /tmp/cookies.txt
```

替换其中的 FILEID 和 FILENAME 即可，FILENAME 自己命名，FILEID 是 Google drive 公开分享的链接中 ID 后面的，例如：`https://drive.google.com/open?id=***ThisIsFileID***` 或 `https://drive.google.com/file/d/***ThisIsFileID***/view?usp=sharing`

- [使用 `curl` 命令下载 Dropbox 文件](https://www.jianshu.com/p/50bccca07d50)：

```
curl -L -o newName.zip https://www.dropbox.com/sh/[folderLink]?dl=1
```

- 将某个文件的前/后 n 行复制到另外一个文件（可构建用于 debug 的小文件）：

```
head -1000 train.txt > train_1000.txt
tail -1000 train.txt > train_1000.txt
```

- 查看一个文件的前 n 行：

```
head -n train.txt
tail -n train.txt
```

- Windows下批量转换CRLF到LF

```
for /R %G in (*) do dos2unix "%G"
```

- 批量将文件名中的oldstring替换为newstring

```bash
for file in `ls`;do mv $file `echo $file|sed 's/oldstring/newstring/g'`;done;
```

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

- 无 sudo 权限下简化 bash [Linux终端bash美化教程](https://www.nenew.net/linux-terminal-bash-mod.html) ：

`export PS1="\[\033[1;32m\]\w\[\033[0m\]\$"`

## Tensorboard

`tensorboard.exe --logdir=\path\to\logs`

- 开其它端口：

`tensorboard.exe --logdir=\path\to\logs --port=6007`

- 远程访问服务器Tensorboard


```bash
ssh -L 16006:127.0.0.1:6006 username@serverIP  # 使用该命令登陆服务器
tensorboard --logdir="/path/to/log-directory  # 在服务器上运行
```

## Jupyter

- [远程访问服务器Jupyter Notebook](https://www.jianshu.com/p/8fc3cd032d3c)，用方法1即可


## Docker

- [只要一小时，零基础入门Docker - 笑虎的文章 - 知乎](https://zhuanlan.zhihu.com/p/23599229)

## tmux

- [tmux：打造精致与实用并存的终端](https://segmentfault.com/a/1190000008188987)

- [Tmux 快捷键 & 速查表 & 简明教程](https://gist.github.com/ryerh/14b7c24dfd623ef8edc7)
- tmux美化：[https://github.com/gpakosz/.tmux](https://github.com/gpakosz/.tmux)
- 创建tmux会话：

`tmux new-session -s <会话名称>`

## bash

- [Bash 脚本教程 - 网道(WangDoc.com)](https://wangdoc.com/bash/)

## nvitop

- [nvitop: An interactive NVIDIA-GPU process viewer](https://github.com/XuehaiPan/nvitop)

## icdiff

- [icdiff: Improved colored diff](https://github.com/jeffkaufman/icdiff)