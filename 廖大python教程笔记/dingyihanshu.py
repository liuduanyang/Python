# 定义函数

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，
# 在缩进块中编写函数体，函数的返回值用return语句返回

def my_abs(x):
	if x>=0:
		return x
	elif x<0:
		return -x

print(my_abs(-5))
# 5


# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None
# return None可以简写为return

>>> def my_hs():
...     i=0
...     while i<10:
...             i=i+1
...             return i
...     return i
...
>>> my_hs()
1

'''
如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下
启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名
（不含.py扩展名
'''

def dayin():
	i=0
	while i<10:
		i=i+1
		print(i)

dayin()
# 打印1~10

def dayin2():
	i=0
	while i<10:
		i=i+1
		print(i)
		if i==5:
			return 

dayin2()
# 打印1~5



# 空函数 什么也不做的函数
def nop():
    pass
# pass语句什么都不做 但是可以用来作为占位符，比如现在还没想好怎么写函数的代码，
# 就可以先放一个pass，让代码能运行起来

# pass还可以用在其他语句里
age = 0 
if age >= 18:
    pass

# 如果想弄一个空函数 还没有pass 就是什么也不写 会报错的



# 参数检查
# 参数个数不对 会报错
# 当参数类型不对时，内置的函数会检查错误  而自己定义的函数则不能检查而导致出错

# 可用内置函数isinstance()实现对参数的检查
def my_abs3(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 如果不是整数或浮点数就会报错 'bad operand type'

my_abs3('a')
# TypeError: bad operand type

print(my_abs3(-0.5))
# 0.5



# 返回多个值 按位置相应的赋值给多个变量  返回多个值相当于返回一个没有括号的tuple
>>> def m():
...     a=0
...     b=1
...     c=2
...     a=b+c
...     b=a+c
...     return a,b
...
>>> va,vm=m()
>>> va
3
>>> vm
5

# 函数参数
# 可在函数定义时，指定默认参数， 调用时只给出x的实参值时 n默认取2 例：求n次方函数 
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 注意：必选参数在前，默认参数在后，否则Python的解释器会报错

# 如果是这样定义的
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

# 如果age为默认 但city不对 实参应该这样输入
enroll('Adam', 'M', city='Tianjin')

# 如果城市为默认城市 年龄不对 则
enroll('Bob', 'M', 7)


# 默认参数必须指向不变对象  不可以是列表  只是说列表不可用作默认参数  但是可以作为参数的
def add_end(L=[]):
    L.append('END')
    return L
# 使用默认参数时(add_end())会出错 因为默认参数那个列表会改变

#　修改如下
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L



# 可变参数
# 计算a2(方) + b2 + c2 + ……
# 由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc([1, 2, 3])
# 14

calc((1, 3, 5, 7))
# 84

#　如果利用可变参数，调用函数的方式可以简化成这样
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，
# 参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入
# 任意个参数，包括0个参数
calc(1, 2)
# 5

calc()
# 0

nums = [1, 2, 3]
calc(*nums)
# 14
# 也可以calc(nums[0], nums[1], nums[2]) 但是麻烦
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见



# 关键字参数
# 关键字参数允许你传入0个或任意个含新的参数名和与其对应的参数值的参数(相当于自己定义一个或多个
# 参数 并给出实参) 这些关键字参数在函数内部自动组装为一个dict

# 定义部分
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
# name: Michael age: 30 other: {}

person('Bob', 35, city='Beijing')
# name: Bob age: 35 other: {'city': 'Beijing'}

person('Adam', 45, gender='M', job='Engineer')
# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

# 如果调用者愿意提供更多的参数，我们也能收到。
# 比如正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字
# 参数来定义这个函数就能满足注册的需求。


'''
和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=extra['city'], job=extra['job'])
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

当然，上面复杂的调用可以用简化的写法：
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
'''

# 对关键字参数进行检查
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


'''
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
这种方式定义的函数如下：

def person(name, age, *, city, job):
    print(name, age, city, job)
和关键字参数**kw不同，命名关键字(可以有默认值)参数需要一个特殊分隔符*，*后面的参数被视为命
名关键字参数。且 * 后面的参数调用时必须赋值 例如：person('liu',18,city='qhd',job='IT')

调用方式如下：

>>> person('Jack', 24, city='Beijing', job='Engineer')
Jack 24 Beijing Engineer

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了

'''


# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


最神奇的是通过一个tuple和dict，你也可以调用上述函数：

>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
'''