# 递归函数
# 计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

# 任何递归函数都存在栈溢出的问题 所以不能递归多次  