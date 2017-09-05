# 函数调用

# abs()函数是系统自带的函数 用来求绝度值 只有一个参数 参数多了少了 参数非法(参数类型不对)都会报错
print(abs(-5))

# max()函数可以接收任意多个参数，并返回最大的那个
print(max(5,10,11,3,2))


# 数据类型转换也是通过函数实现的

# 把其它数据类型转换为整型
print(int('123'))
# 123

print(int(True))
# 1

print(int(13.25))
# 13


# 把其它数据类型转换为浮点型
print(float('13.22'))
# 13.22

print(float(13))
# 13.0

print(float(True))
# 1.0


# 把其它数据类型转换为字符型
print(str(True))
# True          'True'

print(str(13.28))
# 13.28         '13.28'

print(str(521))
# 521           '521'


# 把其它数据类型转换为布尔型
print(bool(0))
# False

print(bool(5))
# True

print(bool(''))
# False

print(bool('0'))
# True


'''
函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，
相当于给这个函数起了一个“别名”：

>>> a = abs      # 变量a指向abs函数
>>> a(-1)        # 所以也可以通过a调用abs函数
1
'''