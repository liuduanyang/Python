#注释

# 单行注释
'''
多行注释
'''


#输入

print('Hello,world')
print('Liu','duanyang')
# print()会依次打印每个字符串，遇到逗号“,”会输出一个空格

print('Liu'+'duanyang')
# + 连接多个字符串

print(300)
print(200+100)
print('100+200=',100+200)


#输出

#Python提供了一个input()函数，可以让用户输入字符串，并存放到一个变量里
name=input()
#当你输入name = input()并按下回车后，Python交互式命令行就在等待你的输入了。这时，你可以输入任意字符，然后按回车后完成输入
#变量可以赋任何值 数字 字母 字符串...
#打印已复制的变量 可以直接输入变量名(以字符串形式打印出来) 也可print(变量名) (常用)

name=input('请输入您的名字：')
print('Hello,',name)
# 输入前带有提示信息