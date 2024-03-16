m = 100  # 设置m的值
print(m)

m = m + 10  # 更新m的值
m = m - 1

sentence = "Hello, m is {}."  # 创建一个字符串，其中包含一个占位符（{}）用于插入变量

formatted_sentence = sentence.format(m)  # 使用字符串的format方法将变量插入到占位符的位置

print(formatted_sentence)  # 使用print函数输出结果
