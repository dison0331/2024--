# 定义一个函数来分解一个正整数的质因数  
def prime_factors(n):
    i = 2  # 从2开始，遍历所有小于或等于n的平方根的数
    factors = []  # 存储质因数的列表  
    while i * i <= n:  # 当i的平方小于或等于n时  
        if n % i:  # 如果n不能被i整除  
            i += 1  # 增加i的值并继续循环  
        else:  # 如果n能被i整除  
            n //= i  # 除以i  
            factors.append(i)  # 将i添加到质因数列表中  
    if n > 1:  # 如果n大于1，说明它本身是一个质因数  
        factors.append(n)  # 将n添加到质因数列表中  
    return factors  # 返回质因数列表


num = int(input('数： '))  # 输入的数字
print(num, "=", " * ".join(str(i) for i in prime_factors(num)))  # 打印出质因数分解的结果
