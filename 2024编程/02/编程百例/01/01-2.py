# 初始化一个空列表来存储三位数
three_digit_numbers = []

# 使用循环和条件判断来生成所有可能的三位数
for hundreds in range(1, 5):  # 百位不能为0
    for tens in range(4):  # 十位剩下的数字
        for ones in range(3):  # 个位剩下的数字
            if (hundreds, tens, ones) not in three_digit_numbers:  # 确保三位数之前没有被添加到列表中
                three_digit_numbers.append((hundreds, tens, ones))

            # 打印所有可能的三位数
for number in three_digit_numbers:
    print(number)