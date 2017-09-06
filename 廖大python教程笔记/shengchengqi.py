# 生成器 generator
# 为了节省空间，不必创建完整的List 而采用能够一边循环一边不断推算出后续的元素的机制：生成器
# 生成器保存的是算法
# 生成器也是可迭代对象

# 生成器的创建
'''
第一种方法
只需将列表生成式的[]改为()即可
>>> l=(i for i in range(1,11))
>>> l
<generator object <genexpr> at 0x000000CC2D633C50>
得到的l这是生成器不是列表 里面存放的是算法



第二种方法
用函数实现
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b                yield是生成器专用的语句 相当于print
        a, b = b, a + b
        n = n + 1
    return 'done'

>>> f = fib(6)
>>> f
<generator object fib at 0x104feaaa0>

'''

# 打印生成器生成列表后的元素
'''
第一种方法
>>> next(l)
1
>>> next(l)
2
>>> next(l)
3
>>> next(l)
4
>>> next(l)
5
>>> next(l)
6
>>> next(l)
7
>>> next(l)
8
>>> next(l)
9
>>> next(l)
10
>>> next(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
通过next()函数一个接一个打印出生成器的下一个返回值
没有更多的元素时，抛出StopIteration的错误
缺点：不方便


第二种方法
>>> for i in l:
...     print(i)
...
1
2
3
4
5
6
7
8
9
10
由于生成器也是可迭代对象所以可以对它进行迭代
'''


def mylist(max):
	i=1
	while i<max:
		yield(i)
		i=i+1
	return 'Over'

o=mylist(11)
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(o)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# <generator object mylist at 0x000000477FF93A40>

for x in o:
	print(x)



'''
但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration
的value中：
>>> g = fib(6)
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
...
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
Generator return value: done
'''

