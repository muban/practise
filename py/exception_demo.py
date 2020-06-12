# 异常捕获
# try:
#     x = int(input("请输入数字"))
# except ValueError:
#     print("请输入数字！")
# finally:
#     x = 3

# try:
#     x = 1 / '1'
# except Exception as e:
#     print(e)
# finally:
#     x = 3

# 自定义异常
try:
    raise NameError('custom error')
except NameError as e:
    print(e)
