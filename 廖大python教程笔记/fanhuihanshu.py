# 返回函数
# 把函数作为结果值返回

# 返回一个求和函数
def lazy_sum(*args):
	def sum():
		ax=0
		for i in args:
			ax=ax+i
		return ax
	return sum

f=lazy_sum(1,3,5,7,9)
print(f())
# 25
# 解析：当我们调用lazy_sum(1,3,5,7,9)时 返回的sum sum指向具体的函数 赋值给f的也就是sum
# 		当我们调用f 即f() 时也就是调用sum得到25  也就是说返回一个函数 并不立即执行这个
#		函数,只有调用时才执行

'''
f是函数（指向函数变量）
>>> f = lazy_sum(1, 3, 5, 7, 9)
>>> f
<function lazy_sum.<locals>.sum at 0x101c6ed90>
''' 

'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部
函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回
的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
'''

# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数,两个或多个函数也不相同
'''
>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False
'''






# 闭包
'''
在上个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部
函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回
的函数中，这种称为“闭包（Closure）”
'''
# 当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
# 返回的函数并没有立刻执行，而是直到调用才执行

# 闭包例子
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())   # 9
print(f2())   # 9
print(f3())   # 9
'''
count()被调用后 执行的过程：先将[]赋值给fs 然后进入for循环,然后在fs列表的末尾插入函数f
这里的f相当于返回值 即return f   这里出现一个闭包  照此步骤 重复循环三次 返回fs列表
此时的fs列表为[f,f,f] 因为返回的是函数f 并非函数调用f()

将count函数的返回值赋值给f1 f2 f3  即 f1=f f2=f f3=f  但fn与f fn与fm之间都不相等
在执行f1() f2() f3()时 由于他们共享父函数 count的变量和参数 所以f函数内的i为3
所以f1() f2() f3()的执行的结果都是9 
'''
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 否则就会和上例一样， 与预期结果不同


# 对上例改进 得到1,4,9
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1())   # 1
print(f2())   # 4
print(f3())   # 9

'''
与上例不同 多了函数f  本例中有两个闭包 一个是count函数内 f是闭包  另一个是 f函数内函数g
是闭包  当执行三次循环是 f内的参数分别为1,2,3  由于g是f的闭包 所以g的变量与f的值相同
所以g内的变量j分别为1,2,3 所以结果分别为1,4,9
'''

# 一个函数可以返回一个计算结果，也可以返回一个函数。

# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量