import math  # 导入math模块

numbers = []  # 创建一个列表

n = 0  # 对变量n进行初始化
m = 0  # 对变量m进行初始化

for i in range(10000000):  # 循环从0到9999999，对每一个数i进行以下操作。
    n = int(math.sqrt(i + 100))  # 计算i+100的平方根并取整，赋值给n。
    m = int(math.sqrt(i + 168 + 100))  # 计算i+168+100的平方根并取整，赋值给m。
    print(f'{i+1}/{1000000}',end='\r')
    if n * n == i + 100 and m * m == i + 168 + 100:  # 判断条件：如果n的平方等于i+100，并且m的平方等于i+168+100，则执行以下操作。
        numbers.append(i)  # 将数加入列表

print('这几个数分别是', numbers)  # 对列表进行输出
