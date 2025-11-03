"""
演示函数基础定义练习案例：自动查核酸
"""


# 定义函数
def check1():
    # 编写函数体输出信息
    print(f"欢迎来到黑马程序员！\n请出示您的健康码以及72小时核酸证明！")


# 调用函数
check1()


# 自定义计算字符串长度
def my_len(str3):
    count = 0
    for i in str3:
        count += 1
    return count


str1 = "sadadadasd"
print(f"{str1}的长度为：{my_len(str1)}")
print(f"{str1}的长度为：{len(str1)}")


# 计算两个数相加

def add(a, b):
    return a + b


print(f"1+2的结果为：{add(1, 2)}")


# 定义函数，接收1个形式参数，数字类型，表示体温
def check(num):
    # 在函数体内进行判断体温
    print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
    if num <= 37.5:
        print(f"体温测量中，您的体温是：{num}度，体温正常请进！")
    else:
        print(f"体温测量中，您的体温是：{num}度，需要隔离！")


# 调用函数，传入实际参数
check(37.6)

"""
当没有定义返回值时，会返回none
"""
print(f"无返回值返回的类型为：{type(check1())}，返回的值为{check1()}")


# None用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    # else:
    #     return None


result = check_age(26)
if not result:
    # 进入if表示result是None值 也就是False
    print("未成年，不可以进入")
else:
    print("已成年")

"""
演示对函数进行文档说明
"""


# 定义函数，进行文档说明
def add(x, y):
    """
    add函数可以接收2个参数，进行2数相加的功能
    :param x: 形参x表示相加的其中一个数字
    :param y: 形参y表示相加的另一个数字
    :return: 返回值是2数相加的结果
    """
    result = x + y
    print(f"2数相加的结果是：{result}")
    return result


add(5, 6)

"""
函数嵌套调用
"""

# 定义函数func_b
def func_b():
    print("---2---")
# 定义函数func_a，并在内部调用func_b
def func_a():
    print("---1---")

    # 嵌套调用func_b
    func_b()

    print("---3---")
# 调用函数func_a
func_a()

"""
变量作用域
    局部变量
    全局变量
"""
"""
演示在函数使用的时候，定义的变量作用域
"""

# 演示局部变量
# def test_a():
#     num = 100
#     print(num)
#
#
# test_a()
# 出了函数体，局部变量就无法使用了
# print(num)

# 演示全局变量
# num = 200
#
# def test_a():
#     print(f"test_a: {num}")
#
# def test_b():
#     print(f"test_b: {num}")
#
# test_a()
# test_b()
# print(num)

# 在函数内修改全局变量
# num = 200
#
# def test_a():
#     print(f"test_a: {num}")
#
# def test_b():
#     num = 500       # 局部变量
#     print(f"test_b: {num}")
#
# test_a()
# test_b()
# print(num)

# global关键字，在函数内声明变量为全局变量
num = 200

def test_a():
    print(f"test_a: {num}")

def test_b():
    global num      # 设置内部定义的变量为全局变量
    num = 500
    print(f"test_b: {num}")

test_a()
test_b()
print(num)
