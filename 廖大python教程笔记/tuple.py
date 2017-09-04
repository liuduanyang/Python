# tuple  :元组

# tuple一旦初始化就不能修改

'''
>>> classmates = ('Michael', 'Bob', 'Tracy')
# 此时classmates这个元组不能进行修改 不能赋值

# 可以调用 同列表list

>>> classmates=('A','B','C')
>>> classmates[0]
'A'
>>> classmates[1]
'B'
>>> classmates[2]
'C'
>>> classmates[-1]
'C'

# 使用tuple 代码更安全

# 当定义的tuple 只有一个元素时 必须按以下方式定义（必须加一个逗号）
>>> t=(1,)
>>> t
(1,)

# 如果t=(1)这样去定义 得到的是1 这个数  因为此时()是一种数学计算符号

# 如果tuple内包含像list这样本身可变的元素 则这个元素可变 但tuple还是不可变的
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
'''