x = input('s')
su1 = int(x[0])
su2 = int(x[1])
su3 = int(x[2])
if (su1 ** 3 + su2 ** 3 + su3 ** 3) == int(x):
    print('Y')
else:
    print('N')
#
# 做法二
# x = int(input("请输入数："))  # 使用input()函数获取用户输入，同时转化为字符串
# x1=(x//100)
# x2=(x//10%10)
# x3=(x%100%10)
# if (x1**3+x2**3+x3**3)==x
#    print('是')
# else:
#    print('不是')
#
# 做法三
# for num in range(100, 1000):
#    num1 = int(num / 100)
#    num2 = int(num % 100) // 10
#    num3 = int(num % 10)
#    if num1 ** 3 + num2 ** 3 + num3 ** 3 == num:
#        print(num)
