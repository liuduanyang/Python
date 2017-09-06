# 列表生成式
list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 带有表达式的列表生成器
[x * x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来

[x+1 for x in range(1,11)]
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# 对带有表达式的列表生成器再进行筛选
[x*x for x in range(1,11) if x%2==0]
# [4, 16, 36, 64, 100]

# 使用两层循环，生成全排列
[m + n for m in 'ABC' for n in 'XYZ']
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


# for循环可以同时使用多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
	print(k,'=',v)
# y = B
# z = C
# x = A

# 同理，列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k, v in d.items()]
# ['z=C', 'y=B', 'x=A']

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
# ['hello', 'world', 'ibm', 'apple']