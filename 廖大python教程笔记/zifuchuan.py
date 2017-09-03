# 字符串

'''
>>> len('a')
1
>>> len('刘端阳')
3
'''



'''
编码问题

encode()将字符转换成字节(bytes)   Python对bytes类型的数据用带b前缀的单引号或双引号表示 b'aBc'
decode()将字节转换成字符

>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> m='中文'.encode('utf-8')
>>> len(m)
6

>>> 'ABC'.encode('ascii')
b'ABC'
>>> n='ABC'.encode('ascii')
>>> len(n)
3

>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'

常常在开头加入以下两行注释
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
'''
print('中文显示正常！')


# 占位符
'''
>>> name=input()
Mike
>>> 'Hello,%s' %name
'Hello,Mike'

>>> name=input()
Mike
>>> print('Hello,%s' %name)
Hello,Mike

>>> print('Hello,%s.I\'m %s' %(name,'Liuduanyang'))
Hello,Mike.I'm Liuduanyang

%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，
后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略

常见的占位符有：
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数



>>> '%2d-%02d' % (3, 1)
' 3-01'
>>> '%.2f' % 3.1415926
'3.14'

其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数


有些时候，字符串里面的%是一个普通字符,这个时候就需要转义，用%%来表示一个%
'''
