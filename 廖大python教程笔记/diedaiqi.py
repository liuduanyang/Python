# 迭代器 Iterator
# 可迭代对象(Iterable):List tuple dict set str generator
# 可迭代对象可用isinstance()函数判断 迭代那章节有

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
'''
可以使用isinstance()判断一个对象是否是Iterable(可迭代的)：

>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False

Iterator(迭代器) 和 Iterable(可迭代的) 不一样

生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

把list、dict、str等Iterable变成Iterator可以使用iter()函数：
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True


所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算  懒得计算长度 懒得多算一步
所以适用于非常非常长的列表 无限长也没关系


'''