# 切片

# 实现取一个list或tuple的部分元素  Python提供了切片（Slice）操作符，能大大简化这种操作

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 去前三个元素
print(L[0:3])
# 表示从序号为0的元素到序号为2(3-1)的元素
# ['Michael', 'Sarah', 'Tracy']

# 如果第一个索引是0，可以省略 即：L[:3]

L[1:3]
# ['Sarah', 'Tracy']
#　表示从序号为１的元素到序号为2(3-1)的元素

# python还支持倒数切片
print(L[-1:])
# ['Jack']

print(L[-3:-1])
# ['Tracy', 'Bob']

print(L[-1:-3])
# 这样不行 是错误的


Z = list(range(100))
print(Z[::5])
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

print(L[:])
# 相当于复制了一个Z

# tuple也可以用切片 操作结果仍然是一个元组
(0, 1, 2, 3, 4, 5)[:3]
# (0,1,2)

# 字符串也可以用切片操作，操作结果仍是字符串
print('ABCDEFG'[:3])
# 'ABC'

'ABCDEFG'[::2]
#'ACEG'