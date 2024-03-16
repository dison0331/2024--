def calculate_distance_and_height(h_now, ci):
    h_all = 0  # 初始化总经过距离
    h_down = h_now  # 当前高度

    for i in range(ci):
        # 球落下
        h_all += h_down

        # 球反弹
        if i < ci - 1:  # 如果不是最后一次反弹，就加上反弹的距离
            h_all += h_down
            h_down /= 2  # 反弹高度是前一次的一半

    return h_all, h_down


# 设置初始高度和反弹次数
initial_height = 100
bounce_count = 10

# 计算总经过距离和最后一次反弹的高度
total_distance, last_bounce_height = calculate_distance_and_height(initial_height, bounce_count)

print(f"球在第{bounce_count}次落地时，共经过了{total_distance}米。")
print(f"第{bounce_count}次反弹的高度是：{last_bounce_height}米。")
