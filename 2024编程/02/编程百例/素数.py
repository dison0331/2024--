# 编写一个Python程序，实现如下功能：判断101-200之间有多少个素数，并输出所有素数。（素数是只能被1或者自己整除的自然数。 ）
def is_prime(n):  # 定义一个判断素数的函数

    if n <= 1:  # 如果n小于等于1，直接返回False，因为1不是素数
        return False

    # 遍历2到n的平方根之间的所有整数，因为如果n不是素数，那么它必定有一个因子小于或等于它的平方根
    for j in range(2, int(n ** 0.5) + 1):

        if n % j == 0:  # 如果n能被j整除，说明n不是素数，返回False
            return False
    return True  # 如果循环结束都没有找到能整除n的数，说明n是素数，返回True


shu = 0  # 初始化素数个数为0

for i in range(101, 201):  # 遍历101到200之间的所有整数
    # 如果i是素数，输出i并增加计数器count的值
    if is_prime(i):
        print(i)
        shu += 1

print("101-200之间共有{}个素数。".format(shu))  # 输出101-200之间素数的个数[format将变量shu的值插入到字符串中指定的位置(占位符{}内)]
