# sorted 排序算法
# sorted()函数就可以对list进行排序 可以对数字 字符 字符串进行排序





# 对含数字的List进行排序

# 按照默认 从小到大排序
sorted([5,3,7,2,1])
# [1, 2, 3, 5, 7]

# 按照指定顺序排序
# key参数可以接收系统函数或自定义函数来实现指定的排序
sorted([-5,-7,6,4,1],key=abs)
# [1, 4, -5, 6, -7]
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序 结合初始的
# 即 key参数就是用接收到的函数处理序列的每一个元素 之后再用sorted函数进行排序
# 序列得到结果





# 对含字符串的序列进行排序
# 按照字符顺序(ASCII码)排序
sorted(['bob', 'about', 'Zoo', 'Credit'])
# ['Credit', 'Zoo', 'about', 'bob']
# 大写字符的ASCII码比较小
# 比较时 先比较第一个字符的大小 如果不同两者间得到一个顺序 如果相同比较第二个字符 

# 将字符串的都变成小写字母 再排序
sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
# ['about', 'bob', 'Credit', 'Zoo']






# 进行反向排序 即从大到小排序  都是用
sorted([1,5,7,3,-6],key=abs,reverse=True)
# [7, -6, 5, 3, 1]
