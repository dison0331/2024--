# 26.利用递归公式求5！
def factorial(n):
    # 递归终止条件
    if n == 0:
        return 1
        # 递归调用
    else:
        return n * factorial(n - 1)

    # 计算5的阶乘


result = factorial(5)
print(result)
