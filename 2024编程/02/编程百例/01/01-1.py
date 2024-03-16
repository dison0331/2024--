lo = 0  # 计数器归零
for i in range(1, 5):  # 百位
    for j in range(1, 5):  # 十位
        for k in range(1, 5):  # 个位
            if i != j and j != k and i != k:
                print(i, j, k)  # 输出所有的数
                lo = lo + 1  # 计数器变更
print('一共有', lo, '个数')  # 计数器总量输出
