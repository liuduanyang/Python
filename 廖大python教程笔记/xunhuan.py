# 循环

# for...in循环
# for x in ...循环就是依次把list或tuple中的每个元素代入变量x，然后执行缩进块的语句
names=['Michael', 'Bob', 'Tracy']
for name in names:
	print(name)

# 结果
# Michael
# Bob
# Tracy

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum=sum+x
print(sum)
# 55

'''
如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，
再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：

>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(5,10))
[5, 6, 7, 8, 9]
'''
sum = 0
for x in list(range(101)):
	sum=sum+x
print(sum)
# 5050



# while循环
# 只要条件满足，就不断循环，条件不满足时退出循环
# 以下两种方法都能实现计算100以内奇数的和

i = 1
sum = 0
while i<100:
	sum=sum+i
	i=i+2
print(sum)


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break
# 在循环中，break语句可以提前退出循环
'''
n = 1
while n <= 100:
    if n > 10:       # 当n = 11时，条件满足，执行break语句
        break        # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
# 执行上面的代码可以看到，打印出1~10后，紧接着打印END，程序结束
'''


# continue
# 在循环中，continue语句可以跳过当前的这次循环
# 实现打印100以内的奇数
n = 0
while n<100:
	n=n+1
	if n%2==0:
		continue
	print(n)
print('END')


# 不要滥用break和continue语句
# 死循环时 用Ctrl+C退出程序