# 序列

string = "abcdefg"

print(string[0:3])

print("你是煞笔 " * 10)

print((2, 20) > (1, 21))

day_string = "你是煞笔" * 2
days = ((1, 20), (2, 12), (3, 20), (4, 25))
day = (2, 13)
# len 元组的个数 filter筛选并定义筛选条件
print(day_string[len(list(filter(lambda x: day > x, days)))])

# 列表
a_list = []
a_list.append("you")
a_list.append("are")
a_list.append("sb")
print(a_list)

# 条件语句
x = "123"
if x == "1":
    print("x的值等于1")
elif x == "123":
    print("x的值等于123")
else:
    print("都不相等")

# user_input = input("请输入\n")
#
# if type(user_input) is str:
#     print("输入的字符串")
# elif type(user_input) is int:
#     print("输入的数字")
# else:
#     print("输入的其他类型")

for x in days:
    print(x)

for i in range(5, 10):
    print("i=%s,i是%s" % (i, i))

num = 5
while True:
    num += 1
    print(num)
    if num > 10:
        break

# 字典
dict_name = "1234567890"
dict1 = {"key", "value"}
print(dict1)

# 推导式
dict1 = {i: "" for i in dict_name}
print(dict1)

b_list = [i * i for i in range(1, 11) if i % 2 == 0]
print(b_list)
