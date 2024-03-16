# 定义一个函数count_chars，输入为一个字符串s
def count_chars(s):
    # 初始化四个计数器
    english = 0  # 英文字母的计数器
    number = 0  # 数字的计数器
    kong = 0  # 空格的计数器
    others = 0  # 其他字符的计数器

    for char in s:  # 遍历字符串s中的每个字符
        if char.isalpha():  # 如果字符是英文字母，则增加英文字母的计数器
            english += 1
        elif char.isdigit():  # 如果字符是数字，则增加数字的计数器
            number += 1
        elif char.isspace():  # 如果字符是空格，则增加空格的计数器
            kong += 1
        else:  # 如果字符既不是英文字母、数字、空格，则增加其他字符的计数器
            others += 1
    return english, number, kong, others  # 返回四个计数的值


s = input("请输入一行字符：")  # 获取用户输入的一行字符
count_letters, count_digits, count_spaces, count_others = count_chars(s)  # 调用函数并获取结果
print(f"英文字母数量：{count_letters}", end=' ')  # 输出英文字母的数量
print(f"数字数量：{count_digits}", end=' ')  # 输出数字的数量
print(f"空格数量：{count_spaces}", end=' ')  # 输出空格的数量
print(f"其他字符数量：{count_others}")  # 输出其他字符的数量
