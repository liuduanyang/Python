'''
当我们从Python官方网站下载并安装好Python 3.5后，我们就直接获得了一个官方版本的解释器：CPython。
这个解释器是用C语言开发的，所以叫CPython。在命令行下运行python就是启动CPython解释器。

>>> 100+200
300
>>> print('Hello,world')
Hello,world
>>> exit()

看到类似C:\>是在Windows提供的命令行模式
在命令行模式下，可以执行python进入Python交互式环境，也可以执行python hello.py运行一个.py文件。
看到>>>是在Python交互式环境下

写一个calc.py的文件，内容如下：
100 + 200 + 300
然后在命令行模式下执行：
C:\work>python calc.py
发现什么输出都没有。
这是正常的。想要输出结果，必须自己用print()打印出来。
'''

print('Hello,wrold')
print(300+200)
exit()