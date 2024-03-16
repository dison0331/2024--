# 18.求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 输入a和n
a = int(input('输入a: '))  # 输入数字a
n = int(input('输入项数n: '))  # 输入需要相加的项数

# 初始化
s = 0
i = a
terms = []  # 用于存储每一项的列表

# 计算s的值并存储每一项
for _ in range(n):  # 根据项数n计算每一项并累加到s
    s += i
    terms.append(i)  # 将当前项添加到列表中
    i = i * 10 + a  # 生成下一个项，如aa, aaa, aaaa

# 输出结果，显示每一项和总和
print("s=", end="")
print("+".join(map(str, terms)), end="")  # 显示每一项，用加号连接
print("=", s)  # 显示总和
