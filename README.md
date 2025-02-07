# PNG-Batch-Compressor

能够自定义参数的 PNG 批量压缩器。[点此](https://github.com/ZexWoo/PNG-Batch-Compressor/blob/main/PNG-Batch-Compressor.py) 下载 Python 脚本，注意该脚本采用 GPL-3.0 开源协议。

**温馨提示：这是我的习作，如有不足，请见谅。**

## 用法

### 准备好 oxipng

首先，你需要下载 oxipng 这款压缩器。

[点此](https://github.com/shssoichiro/oxipng/releases) 下载适合你设备的版本。

下载后，解压到你觉得便于管理的目录。

将 `oxipng-9.1.3-x86_64-pc-windows-msvc` 文件夹所在的目录加入系统的 Path 环境变量：

1. 右键单击「开始」按钮。
2. 单击「系统」。
3. 单击「高级系统设置」。
4. 单击「环境变量…」。
5. 在「系统变量」一栏，选中「Path」所在的一栏。
6. 单击「编辑…」。
7. 单击「新建」。
8. 将 `oxipng-9.1.3-x86_64-pc-windows-msvc` 文件夹所在的目录粘贴到新增的这一栏。
9. 单击「确定」三次，关掉所有窗口。

确认 oxipng 已能成功运作：

1. 右键单击「开始」按钮。
2. 单击「终端」。
3. 输入 `oxipng`，然后回车。
4. 如果展示下列信息，则说明成功。

```
error: the following required arguments were not provided:
  <files>...

Usage: oxipng.exe <files>...

For more information, try '--help'.
```

### 开始压缩图片

将 `PNG-Batch-Compressor.py` 复制粘贴到你计划压缩 PNG 的目录，运行它。

它会创建 `Input` 和 `Output` 两个文件夹。

将待压缩的所有 PNG 都拖入 `Input` 文件夹中。

再次运行 `PNG-Batch-Compressor.py`，在每一步按提示操作，输入符合你需求的值；抑或是简单地摁下「回车」按钮使用默认参数压缩。

压缩完毕的文件会出现在 `Output` 文件夹中以对应压缩参数命名的子文件夹中。
