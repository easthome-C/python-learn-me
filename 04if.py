"""
判断语句

"""
import random

# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}, 类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}, 类型是：{type(bool_2)}")
# 比较运算符的使用
# == , !=, >, <, >=, <=
# 演示进行内容的相等比较
num1=10
num2=10
print(f"10==10结果为：{num1==num2}")
num1=10
num2=20
print(f"10==10结果为：{num1==num2}")

# 演示大于小于，大于等于小于等于的比较运算
if num1==num2:
    print(f"num1==num2")
elif num1>num2:
    print(f"elif num1>num2:")
elif num1<num2:
    print(f"num1<num2")
else:
    print(f"哈哈")


# 键盘输入年龄判断是否成年

age=int(input("输入年龄："))
if age>= 18:
    print(f"你已经{age}岁，已经成年了")
else:
    print(f"你才{age}岁，还是未成年！！！")


# 判断语句嵌套

print("=====================判断语句嵌套=================")
if int(input("你的身高是多少：")) > 120:
    print("身高超出限制，不可以免费")
    print("但是，如果vip级别大于3，可以免费")

    if int(input("你的vip级别是多少：")) > 3:
        print("恭喜你，vip级别达标，可以免费")
    else:
        print("Sorry 你需要买票10元")
else:
    print("欢迎小朋友，免费游玩。")

# 随机生成一个数字，键盘输入猜数字

# 构建一个随机数字
num= random.randint(1,10)

guess_num=int(input("输入你猜测的数字："))
if guess_num == num1:
    print(f"恭喜你一次猜中")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")

    guess_num = int(input("再次输入你要猜测的数字："))

    if guess_num == num:
        print("恭喜，第二次猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")

        guess_num = int(input("第三次输入你要猜测的数字："))

        if guess_num == num:
            print("第三次猜中了")
        else:
            print("三次机会用完了，没有猜中。")

for i in range(0,11):
    guess_num=int(input("输入数字:"))
    if  guess_num== num:
        print(f"恭喜{guess_num}猜对了")
        break
    elif guess_num>num:
        print(f"输入的{guess_num}大了")
    else:
        print(f"输入的{guess_num}小了")


