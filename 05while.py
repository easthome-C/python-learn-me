"""
演示while循环基础练习题：求1-100的和
"""
import random

sum = 0
i = 1
while i<=100:
    sum += i
    print(sum)
    i += 1

print(f"1-100累加的和是：{sum}")


num = random.randint(1,10)
print(f"随机数为{num}")
guess_num = int(input("输入数字:"))
if guess_num == num:
    print(f"恭喜你一次猜中")
else:
    while guess_num != num:
        if guess_num > num:
            guess_num = int(input(f"输入的{guess_num}大了，重新输入："))
        else:
            guess_num = int(input(f"输入的{guess_num}小了，重新输入："))
    print(f"恭喜你{guess_num}是正确的！")


# while循环嵌套
i = 1
while i <= 100:
    print(f"今天是第{i}天，准备表白.....")

    # 内层循环的控制变量
    j = 1
    while j <= 10:
        print(f"送给小美第{j}只玫瑰花")
        j += 1

    print("小美，我喜欢你")
    i += 1

print(f"坚持到第{i - 1}天，表白成功")

# 九九乘法表
i = 1
while i <= 9:

    # 定义内层循环的控制变量
    j = 1
    while j <= i:
        # 内层循环的print语句，不要换行，通过\t制表符进行对齐
        print(f"{j} * {i} = {j * i}\t", end='')
        j += 1

    i += 1
    print()     # print空内容，就是输出一个换行