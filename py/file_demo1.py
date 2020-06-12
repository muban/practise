# 文件内建函数和方法
#     open() 打开文件
#     read() 输入
#     readline() 输入一行
#     seek() 文件内移动
#     write() 输出
#     close() 关闭文件

# # 打开并写入文件
# file1 = open("file_name.txt", "w")
# file1.write("姓名")
# file1.close()
#
# # 打开并读取文件
# file2 = open("file_name.txt")
# print(file2.read())
# file2.close()
#
# # 打开文件并增加内容
# file3 = open("file_name.txt", "a")
# file3.write(":木大")
# file3.close()

# # 打开文件并逐行读取
# file4 = open("file_name.txt")
# for line in file4.readlines():
#     print("%s\n=====" % line)
# file4.close()

# # 文件指针与指针移动
# file5 = open("file_name.txt")
# print(file5.readline())
# print("读取一排内容后的指针位置：%s" % file5.tell())
# file5.seek(0)
# # 第一个参数是偏移量，第二个参数是偏移开始的位置
# file5.seek(1, 1)
# print("重置后指针位置：%s" % file5.tell())
# file5.close()
