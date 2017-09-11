# 匿名函数

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

# lambda x: x * x 表示一个匿名函数 lambda是匿名函数的关键字   : 前面的x表示参数 ：后面的是
# 匿名函数的表达式语句
# 匿名函数只能有一个表达式，不用写return，返回值就是该表达式的结果

'''
lambda x: x * x

等价于：

def f(x):
    return x * x
'''

# 匿名函数不用担心命名冲突 因为它没有名字

# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f=lambda x: x*x
print(f(9))
print(f)
# 81
# <function <lambda> at 0x000000F93DA46048>

# 也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y


# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数