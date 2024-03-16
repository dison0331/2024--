#  25.求1+2!+3!+…+20!的和
he = 0  # 初始化求和变量
factorial = 1  # 初始化阶乘变量为1（0的阶乘是1，但这里我们从1开始）

# 累加1到20的阶乘
for b in range(1, 21):
    factorial *= b  # 更新阶乘值（累乘）
    he += factorial  # 将当前阶乘值加到总和中
    
print(he)  # 输出最终的和
