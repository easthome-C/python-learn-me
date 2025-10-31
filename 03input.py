"""
程序输入

input()从键盘获取输入数据
"""

print("输入数字")
a=input()
print(f"输入的数字为：{a}")
print(f"输入的数字为：{type(a)}")

name=input("键盘输入：")
print("键盘录入的是：%s" % name)

# 输入纯数字
num=input("输入纯数字：")
print("录入的数据类型为%s,数据转换后为：%s" % (type(num),type(int(num))),num)