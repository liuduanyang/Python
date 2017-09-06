# 迭代 （Iteration）
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代
# Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上 比如dict、字符串、
# 或者一些我们自定义的数据类型
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)
# b
# a
# c
# 因为字典存储是无序的 所以每次得到的顺序可能会不同

# for key in d               迭代key-value的key
# for value in d.values()    迭代value
# for k, v in d.items()      迭代key-value

for value in d.values():
	print(value)

for k, v in d.items():
	print(k)
	print(v)


# 对字符串进行迭代
for num in 'Liuduanyang':
	print(num)


# 通过collections模块的Iterable类型判断一个对象是否是可迭代对象

from collections import Iterable
print(isinstance('abc', Iterable))
# True

print(isinstance([1,2,3], Iterable))
# True

print(isinstance(123, Iterable))
# False
# 可通过某个个例来判断该数据类型是否是可迭代对象


# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一
# 个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
# 0 A
# 1 B
# 2 C