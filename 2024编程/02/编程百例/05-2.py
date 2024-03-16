da = 0
xiao = 0
kong = 1
a = float(input("请输入第一个数："))  # 使用input()函数获取用户输入，同时用float()函数将输入的字符串转换为浮点数
da = xiao = a
b = float(input("请输入第二个数："))  # 使用input()函数获取用户输入，同时用float()函数将输入的字符串转换为浮点数
if b > da:
    kong = da
    da = b
    xiao = kong
c = float(input("请输入第三个数："))  # 使用input()函数获取用户输入，同时用float()函数将输入的字符串转换为浮点数
if c > da:
    kong = da
    da = c
    c = kong
else:
    if c > xiao:
        print(da, c, xiao)
    else:
        print(da,xiao,c)
