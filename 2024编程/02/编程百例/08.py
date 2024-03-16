
# 输出9*9乘法表
for i in range(1, 10):  # 外层循环，i的值从1到9
    for j in range(1, i + 1):  # 内层循环，j的值从1到i（包括i）
        print(j, '*', i, '=', i * j, end='    ')  # 打印乘法表达式，并添加到当前行的末尾
    print('  ')
