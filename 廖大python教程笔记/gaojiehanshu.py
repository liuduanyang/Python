# 高阶函数


# 函数名也是变量
print(abs(-5))
# 5

myabs=abs
print(myabs(-5.5))
# 5.5

abs=10
print(abs)
# 10

print(myabs(-4.5))
# 4.5



# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，
# 这种函数就称之为高阶函数

def add(x,y,f):
    return f(x)+f(y)

print(add(-5,6,abs))
# 11
# 要想执行成功 需要把前面abs=10的语句注释掉

# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式