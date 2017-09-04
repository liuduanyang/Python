# 条件判断

age=20
if age >= 18:
	print('您的年龄是%d' %age)
	print('您是成年人')

'''
如果age=input('请输入您的年龄：') 这样的到的age是一个字符串
'''


age=16
if age >= 18:
	print('您的年龄是%d' %age)
	print('您是成年人')
else:
	print('您的年龄是%d' %age)
	print('您是未成年人')


age=3
if age >= 18:
	print('您是成年人')
elif age >= 12:
	print('您是青少年')
else:
	print('您是小孩子')


'''
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# teenager
'''


'''
if判断条件还可以简写，比如写：

if x:
    print('True')

只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False

if 'a':
	print('True')

# True
'''

# Python提供了int()函数来将字符串数据类型转换成整数类型
# 注意 int()函数只能转换只含有数字的字符串 
# int()函数发现一个字符串并不是合法的数字时就会报错，程序就退出了

age = input('请输入您的年龄：')
if int(age) >= 18:
	print('您是成年人')
else:
	print('您是未成年人')