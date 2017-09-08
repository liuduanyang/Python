# reduce函数

'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

'''

# 比如，求一个序列的和
from functools import reduce
def add(x,y):
	return x+y
print(reduce(add,[1,3,5,7,9]))
# 25
# 运算过程：先取出1,3求和 再把结果4赋值给x 取5位y 依次计算 最终得到结果


# 实现把str转换成int
from functools import reduce
def fn(x,y):
	return x*10+y
def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
print(reduce(fn,map(char2num,'13579')))
# 13579

'''
将上述过程整理成一个函数
from functools import reduce

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

注意：s的区别 str2int(s) 和 map(char2num, s) 的s是一个s都是调用时给出的字符串
	  而 char2num(s)中的 s 是指map函数遍历调用给出的字符串时依次得到的字符串
	  比如 给出'13579' 那么第一个s就是'13579' 而  char2num(s)中的s依次表示'1' '3' '5' '7'
	  '9'
'''