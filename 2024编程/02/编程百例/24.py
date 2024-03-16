# 24.有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和
def fibonacci_fraction_sum(n):  # 定义一个函数fibonacci_fraction_sum，它接受一个参数n，表示要计算数列的前n项之和

    z, m = 2, 1  # 初始化前两个分数
    sum_fractions = 0  # 初始化一个变量sum_fractions，用于存储数列前n项的和，初始值为0。

    # 计算前n项的和
    for _ in range(n):  # 使用for循环迭代n次，计算数列的前n项。
        sum_fractions += z / m  # 在循环的每次迭代中，将当前的分数a/b加到sum_fractions上。

        # 计算下一个分数
        z, m = z + m, z  # 这是数列生成的关键部分。这里同时更新a和b的值。a的新值是a和b的和（即斐波那契数列的下一个数），b的新值是旧的a值。

    return sum_fractions  # 函数返回数列前n项的和。


# 计算前20项的和
total_sum = fibonacci_fraction_sum(20)
# 调用上面定义的函数，传入参数20，计算数列的前20项之和，并将结果存储在total_sum变量中。

print(f"数列的前20项之和为: {total_sum}")
# 使用print函数输出数列前20项的和。这里使用了f-string格式化字符串，将total_sum的值插入到输出的字符串中。
