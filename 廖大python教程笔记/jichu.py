# python编程基础

a = 100
if a >= 0:
    print(a)
else:
    print(-a)
# 当语句以冒号:结尾时，缩进的语句视为代码块(相当于{}内的语句)

# Python程序是大小写敏感的





# 数据类型和变量
'''
 数据类型：整数
		   浮点数
		   字符串('' 或 ""括起来的文本)
		   		"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符
		   		'I\'m \"OK\"!' 表示的字符串内容是：I'm "OK"!
			
		   布尔值(在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来)
            >>> True
			True
			>>> False
			False
			>>> 3 > 2
			True
			>>> 3 > 5
			False
			>>> True and True
			True
			>>> True and False
			False
			>>> False and False
			False
			>>> 5 > 3 and 3 > 1
			True
			>>> not True
			False
			>>> not False
			True
			>>> not 1 > 2
			True

			or 的就不写了


			空值 空值是Python里一个特殊的值，用None表示
'''

# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
# Python还允许用r''表示''内部的字符串默认不转义  	>>> print(r'\\\t\\') 输出：\\\t\\
			
'''

>>> print('''line1
... line2
... line3''')
line1
line2
line3

'''


# 变量

#同一个变量可以反复赋值，而且可以是不同类型的变量

# 常量
# 常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：PI = 3.14159265359
# 其实常量也是变量，可以改变值

# 除法
# 用/得到的值是浮点数
# 用//得到的值是整数(只取结果的整数部分)

# 取余
10 % 3
#得 1
