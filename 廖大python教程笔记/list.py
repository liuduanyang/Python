# list 数组数据类型
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素

'''
# 定义
>>> classmates = ['A', 'B', 'C']
>>> classmates
['A', 'B', 'C']

# 索引
>>> classmates=['A','B','C']
>>> classmates
['A', 'B', 'C']
>>> classmates[0]
'A'
>>> classmates[1]
'B'
>>> classmates[2]
'C'
>>> classmates[-1]
'C'
>>> classmates[-2]
'B'
>>> classmates[-3]
'A'

# 算长度
>>> len(classmates)
3

# 往list中追加元素到末尾
>>> classmates=['A','B','C']
>>> classmates.append('D')
>>> classmates
['A', 'B', 'C', 'D']

# 把元素插入到指定的位置
>>> classmates=['A','B','C']
>>> classmates.insert(1,'D')
>>> classmates
['A', 'D', 'B', 'C']

# 删除list末尾的元素
>>> classmates=['A','B','C']
>>> classmates.pop()
'C'
>>> classmates
['A', 'B']

# 删除指定位置的元素
>>> classmates=['A','B','C']
>>> classmates.pop(1)
'B'
>>> classmates
['A', 'C']

# 把某个元素替换成别的元素
>>> classmates=['A','B','C']
>>> classmates[1]='E'
>>> classmates
['A', 'E', 'C']

# list里面的元素的数据类型也可以不同
>>> L = ['Apple', 123, True]

# list元素也可以是另一个list
>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
>>> len(s)
4

'php'的表示方法 s[2][1]   
空数组的长度为0
'''
classmates=['A','B','C']
classmates.insert(1,'D')
print(classmates)