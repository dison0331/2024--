# 获取用户输入的年、月和日并转换为整数类型。
year = int(input('请输入年份: '))
month = int(input('请输入月份: '))
day = int(input('请输入日期: '))

# 判断用户输入的月份是否在1-12之间，如果不是，则输出错误信息并提示重新输入。
while True:

    if month < 1 or month > 12:
        print("无效的月份！请输入1-12之间的数字")
        month = int(input('请输入重新月份: '))  # 要求从新输入
    else:
        break  # 如果月份有效，则退出循环

# 判断是否是闰年，如果是闰年，二月的天数为29天，否则为28天
is_leap_year = False  # 判断年份是否为闰年，如果是，则将is_leap_year设置为false。
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    is_leap_year = True  # 判断年份是否为闰年，如果是，则将is_leap_year设置为True。

days_in_month = [31, 28 if not is_leap_year else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 定义一个列表days_in_month，表示每个月的天数。如果年份是闰年，二月的天数为29天，否则为28天。

total_days = sum(days_in_month[:month - 1]) + day  # 计算从年初到指定日期（不包括指定日期）的总天数。

print(f"{year}年的{month}月{day}日是这一年的第{total_days}天")  # 输出指定日期是这一年的第几天。
