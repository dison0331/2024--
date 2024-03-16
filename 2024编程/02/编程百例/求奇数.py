# 初始化一个计数器变量，用于遍历数字
n = 0
while n <= 100:  # 使用while循环，从0开始遍历数字，直到100

    if n % 2 != 0:  # 如果当前数字是奇数（即除以2的余数不等于0），则打印该数字
        print(n)

    n += 1  # 计数器加1，继续遍历下一个数字

# for i in range(101):
#    if i % 2 != 0:
#        print(i)

# for a in range(1,100,2):
#    print(a)
