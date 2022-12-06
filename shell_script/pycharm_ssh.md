# PyCharm 连接远程服务器

## 有跳板机时的ssh连接

### 一、配置跳板机

首先使用 ssh 连接跳板机（jump server），找到 ~/.ssh/config 文件输入以下内容（如果没有找到就直接创建一个 config 文件）：

```bash
Host *
    ControlPersist yes
    ControlMaster auto
    ControlPath ~/.ssh/master-%r@%h:%p
```

保存后退出，使用跳板机连接一次远程解释器所在的服务器：

```bash
ssh -p <server_port> <username>@<server_ip>
```

### 二、本地配置

打开cmd，输入以下命令：

```bash
ssh -N -f -L 6000:<server_ip>:<server_port> -p <jump_port> <jump_username>@<jump_ip> -o TCPKeepAlive=yes
# 多个跳板机时：
ssh -N -f -L 6000:<server_ip>:<server_port> -p <jump_port> <jump_username1>@<jump_ip1>,<jump_username2>@<jump_ip2> -o TCPKeepAlive=yes
```

通过以上方式我们就建立起了 localhost:6000 到 <server_ip>:<server_port> 的映射，其中 `-L` 是通过“本地转发”方式建立 ssh 隧道；`-N` 使跳板机连接远程服务器后，并不打开shell；`-f` 使命令行窗口关闭后，仍在后台运行，需要和 `-N` 配合使用。此时关闭 cmd 窗口也不会停止 ssh 隧道了。

### 三、配置pycharm remote interpreter

在配置时，把 SSH interpreter 的 host 设置为 127.0.0.1（设为localhost可以吗？TODO），port 为 6000 就可以了。

### Reference：

- [windows下pycharm通过跳板机使用远程解释器remote interpreter](https://www.jianshu.com/p/afe423602ce3)
- [pycharm + ssh 跳板机 + 服务器](http://jjkislele.cn/2019/08/22/2019-08-22-usage-pycharm-ssh/)
- [190424-PyCharm通过跳板机连接远程服务器](https://blog.csdn.net/qq_33039859/article/details/89503464)