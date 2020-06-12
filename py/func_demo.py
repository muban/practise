def func(self):
    print("func test %s" % self)


func("参数")


# *表示可变长参数
def func_change(first, *other):
    print('第一个参数为：%s 可变参数长度：%s' % (first, len(other)))


func_change(1, 2, 3, 4, 5, 6)

with open('name.txt') as names:
    for name in names.read().split('、'):
        print(name)

# 生成器与迭代器
# 迭代器
a_list = [1, 2, 3]
it = iter(a_list)
while True:
    try:
        print(next(it))
    except Exception as e:
        print(e)
        break


# 生成器 yield记录当前值
def frange(start, stop, step):
    temp = start
    while temp < stop:
        yield temp
        temp += step


for i in frange(10, 20, 0.5):
    print(i)


# 测试yield 生成器，yield具备return的作用，具体为返回并停止在当前位置
def test_yield(nums):
    for num in range(0, nums, 2):
        yield num
        print('next')


test_iter = test_yield(10)
# print(next(test_iter))
for i in test_iter:
    print(i)
