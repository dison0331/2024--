def find_perfect_numbers(limit):
    ok_numbers = []  # 初始化一个空列表，用于存储完数

    # 遍历1到limit之间的所有数
    for num in range(1, limit + 1):
        sum_of_divisors = 0  # 初始化因子和为0

        # 只检查到num的平方根，因为一个大于平方根的因子必定有一个小于平方根的配对因子
        for i in range(1, int(num ** 0.5) + 1):
            # 如果i是num的因子
            if num % i == 0:
                # 将i添加到因子和中
                sum_of_divisors += i

                # 如果i不等于num除以i的商（即不是平方根），则将其也添加到因子和中
                if i != num // i:
                    sum_of_divisors += num // i

                    # 如果因子和等于num本身，则num是一个完数
        if sum_of_divisors == num:
            ok_numbers.append(num)  # 将完数添加到列表中

    return ok_numbers  # 返回完数列表


# 调用函数，找出1000以内的所有完数
perfect_numbers = find_perfect_numbers(1000)

print("1000以内的完数有:", perfect_numbers)
