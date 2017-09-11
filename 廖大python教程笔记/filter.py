# filter
# filter()函数用于过滤(筛选)序列
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数
# 依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 给定list删掉偶数 保留奇数
L=[1, 2, 4, 5, 6, 9, 10, 15]
def dub(n):
	return n%2==1
list(filter(dub,L))
# [1, 5, 9, 15]

# filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要
# 用list()函数获得所有结果并返回list

# 筛选奇数
def jis(n):
	return (n+1)%2==1
list(filter(jis,L))
# [2, 4, 6, 10]