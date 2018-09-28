def main():
    # 获取用户输入的文件名称:xxx.txt
    file_name = input("请输入要复制的文件名称：")
    # 打开文件，r
    file = open(file_name, "rb")
    # 创建新文件，w，xxx(复件).txt
    head, S, tail = file_name.rpartition(".")
    new_file_name = head + "(复件)" + S + tail
    new_file = open(new_file_name, "wb")

    while True:
        # 读取文件内容
        s = file.read(1024)
        if len(s) == 0:
            break
        # 将文件内容写入新文件。
        new_file.write(s)

    # 关闭文件
    file.close()
    new_file.close()


main()
