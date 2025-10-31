"""
演示Python for循环临时变量的作用域
"""
i = 0
for i in range(5):
    print(i)

print(i)


"""
演示for循环打印九九乘法表
"""

# 通过外层循环控制行数
for i in range(1, 10):
    # 通过内层循环控制每一行的数据
    for j in range(1, i + 1):
        # 在内层循环中输出每一行的内容
        print(f"{j} * {i} = {j * i}\t", end='')

    # 外层循环可以通过print输出一个回车符
    print()
"""
演示for循环的练习题：数一数有几个a
"""
# 统计如下字符串中，有多少个字母a
name = "itheima is a brand of itcast"

# 定义一个变量，用来统计有多少个a
count = 0

# for 循环统计
# for 临时变量 in 被统计的数据:
for x in name:
    if x == "a":
        count += 1

print(f"被统计的字符串中有{count}个a")


"""
演示Python中的range()语句的基本使用
"""

# range语法1 range(num)
# for x in range(10):
#     print(x)

# range 语法2 range(num1, num2)
# for x in range(5, 10):
#     # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间间隔是1
#     print(x)

# range 语法3 range(num1, num2, step)
# for x in range(5, 10, 2):
#     # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间的间隔是2
#     print(x)

for x in range(10):
    print("送玫瑰花")

"""
演示循环语句的中断控制：break和continue
"""
import random
num = random.randint(1, 10)



# 演示循环中断语句 continue
# for i in range(1, 6):
#     print("语句1")
#     continue
#     print("语句2")

# 演示continue的嵌套应用
# for i in range(1, 6):
#     print("语句1")
#     for j in range(1, 6):
#         print("语句2")
#         continue
#         print("语句3")
#
#     print("语句4")

# 演示循环中断语句 break
# for i in range(1, 101):
#     print("语句1")
#     break
#     print("语句2")
#
# print("语句3")


# 演示break的嵌套应用
for i in range(1, 6):
    print("语句1")
    for j in range(1, 6):
        print("语句2")
        break
        print("语句3")

    print("语句4")