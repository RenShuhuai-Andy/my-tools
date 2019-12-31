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

- 寻找GPU利用率瓶颈 ([参考](https://zhuanlan.zhihu.com/p/53345706))：

`watch -n 0.1 nvidia-smi`

- 查看GPU型号：

`lspci | grep -i vga`

### 内存查询

`free`

### 文件（夹）大小查询

- 查看当前文件夹大小

`du -sh`

- 查看某个文件（夹）大小查询

`du -h file/folder`

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
# 可以使用 conda 时：
conda create -n env_name -y python=3.6
source activate env_name
source deactivate
conda install -n env_name -y package_name
conda remove -n env_name --all
conda remove --name env_name package_name
# 无法使用 conda 连网时：
python3 -m venv env_name
source env_name/bin/activate
deactivate
```

- 命令行 pdb 调试

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

- 使用 `scp` 命令进行上传下载

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

## Docker

[只要一小时，零基础入门Docker - 笑虎的文章 - 知乎](https://zhuanlan.zhihu.com/p/23599229)

## tmux

[tmux：打造精致与实用并存的终端](https://segmentfault.com/a/1190000008188987)

[Tmux 快捷键 & 速查表 & 简明教程](https://gist.github.com/ryerh/14b7c24dfd623ef8edc7)

- 创建tmux会话：

`tmux new-session -s <会话名称>`