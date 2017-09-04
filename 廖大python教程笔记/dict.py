# 字典
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）
# 存储，具有极快的查找速度。这种查找速度都非常快，不会随着字典大小的增加而变慢

d={'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])
# 95

# 除了上述初始化方法外，还可以通过key来放入数据
d['Adam']=67
print(d['Adam'])
print(d)
# 67
# {'Adam': 67, 'Michael': 95, 'Bob': 75, 'Tracy': 85}


# 一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Adam']=67
d['Adam']=99
print(d['Adam'])
# 99


# 通过in判断key是否存在
print('Tracy' in d)
# True


# 通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Bob'))
# 75

print(d.get('Mary'))
# None
# 返回None的时候Python的交互式命令行不显示结果

print(d.get('Mary',0))
# 0
# Mary不在时返回0 如果不指定0 则返回None且在交互命令行不显示

# 删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')
print(d)
#{'Michael': 95, 'Tracy': 85, 'Adam': 99}

# dict内部存放的顺序和key放入的顺序是没有关系的

'''
和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的
第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混
乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心
地作为key。而list是可变的，就不能作为key
'''