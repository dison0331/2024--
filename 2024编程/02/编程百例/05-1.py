x = float(input("请输入第一个数："))  # 使用input()函数获取用户输入，同时用float()函数将输入的字符串转换为浮点数
y = float(input("请输入第二个数："))  # 使用input()函数获取用户输入，同时用float()函数将输入的字符串转换为浮点数
z = float(input("请输入第三个数："))  # 使用input()函数获取用户输入，同时用float()函数将输入的字符串转换为浮点数
# 请求用户输入三个整数

numbers = [x, y, z]  # 创建一个包含这三个数的列表
numbers.sort()  # 对列表进行排序，默认是升序排序，即从小到大
# 使用内置的sort()函数对这三个数进行排序（修改原表而不是新建表）

print("从小到大排序后的结果为：", numbers)  # 输出排序后的结果，使用print()函数和字符串格式化
