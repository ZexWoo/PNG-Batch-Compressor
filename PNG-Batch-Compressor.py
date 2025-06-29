import os
import time

def findext(dir, exts):
    """输入目录和所需拓展名，返回目录和子目录中所有符合条件的文件名列表。"""
    allfile = []
    for path_name, folder_names, files in os.walk(dir):
        for file in files:
            allfile.append(os.path.join(path_name, file))
    # 返回过滤器对象
    files_filter = filter(lambda x: os.path.splitext(x)[1] in exts, allfile)
    file_list = list(files_filter)
    return file_list

def optimization_selector():
    """选择压缩力度。"""
    number = input("选择压缩力度，越大则体积越小，速度越慢（0~7）：")
    match number:
        case "0":
            optimization = '-o 0 '
        case "1":
            optimization = '-o 1 '
        case "2":
            optimization = '-o 2 '
        case "3":
            optimization = '-o 3 '
        case "4":
            optimization = '-o 4 '
        case "5":
            optimization = '-o 5 '
        case "6":
            optimization = '-o 6 '
        case "7":
            optimization = '-o max '
        case _:
            optimization = ''
    return optimization

def interlacing_selector():
    """设置是否使用交错，交错会增大体积。"""
    number = input("是否使用交错（0=去除交错，1=使用交错，回车保持原样）：")
    match number:
        case "0":
            interlacing = '-i 0 '
        case "1":
            interlacing = '-i 1 '
        case _:
            interlacing = '-i keep '
    return interlacing

def strip_selector():
    """选择元数据的去除方案，去除无关元数据可以减小体积。"""
    number = input("""选择元数据的去除方案：
0=不去除
1=仅去除不影响图片渲染的元数据
2=去除所有对图片不重要的元数据
你的选择是：""")
    match number:
        case "1":
            strip = '--strip safe'
        case "2":
            strip = '--strip all'
        case _:
            strip = ''
    return strip

def param_selector():
    """设置压缩参数。"""
    param = ''
    auto = input("回车以使用 oxipng 默认设置，输入 1 手动设置一些选项：")
    if auto:
        optimization = optimization_selector()
        interlacing = interlacing_selector()
        strip = strip_selector()

        param += optimization + interlacing + strip
    else:
        param = ''

    return param

if __name__ == '__main__':
    # 获取当前目录
    current_path = os.getcwd()

    # 确认输入目录是否存在，如不存在，则创建
    input_path = current_path + '\\Input'
    if not os.path.exists(input_path):
        os.mkdir('./Input')
        print("「Input」文件夹不存在，已帮你创建好！")

    # 确认输出目录是否存在，如不存在，则创建
    output_path = current_path + '\\Output'
    if not os.path.exists(output_path):
        os.mkdir('./Output')
        print("「Output」文件夹不存在，已帮你创建好！")

    # 支持的输入文件扩展名
    exts = ['.png', '.PNG']

    # 获得待处理的文件列表
    files = findext(input_path, exts)

    if files:
        param = param_selector()

        total_start = time.time()

        for path in files:
            # 获取输出文件名
            dirStr, ext = os.path.splitext(path)
            png_name = dirStr.split('\\')[-1]

            # 调用 oxipng
            if param:
                command = f"oxipng {param} --dir=\"{output_path}\\{param}\" \"{path}\""
            else:
                command = f"oxipng {param} --dir=\"{output_path}\\default param\" \"{path}\""
            print(f"使用的命令为：\n\n{command}\n")
            start = time.time()
            os.system(command)
            end = time.time()
            print(f"\n共 {len(files)} 张，已完成第 {files.index(path) + 1} 张「{png_name}」，耗时约 {round((end - start), 1)} 秒。\n{'-' * 30}")

        total_end = time.time()
        print(f"所有压缩任务已完成！总耗时约 {round((total_end - total_start), 1)} 秒。")
    else:
        print("待压缩 PNG 目录为空！请将需要压缩的 PNG 都存放到 Input 文件夹中！")