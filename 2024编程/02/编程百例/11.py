# 11.兔子繁殖问题——本质为斐波那契数列（略）

# 定义一个函数，用于计算第n个斐波那契数
def fibonacci(n):
    if n == 1:  # 如果n等于1，返回0
        return 0
    elif n == 2:  # 如果n等于2，返回1
        return 1
    else:  # 对于其他的情况，使用递归计算第n个斐波那契数
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 11):  # 通过循环从1到10打印出斐波那契数列的每一个数
    print(fibonacci(i))
