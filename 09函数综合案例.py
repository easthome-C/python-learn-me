"""
综合案例
    全局变量money 为银行卡余额 50000000
    name客户姓名，键盘输入
"""

money = 50000000
name = input("请输入客户姓名：")


def query():
    """
    查询余额
    :return: 返回银行卡余额
    """
    return money

def add(num):
    """
    存款函数
    :param num: 存款金额
    :return: 银行卡余额
    """
    global money
    money += num
    return money
def sub(num):
    """
    取款函数
    :param num: 取款金额
    :return: 银行卡余额
    """
    global money
    money -= num
    return money

# 定义主菜单函数
def main():
    print(f"欢迎{name}")
    print("查询余额\t请输出【1】")
    print("存款业务\t请输出【2】")
    print("取款业务\t请输出【3】")
    print("退出系统\t请输出【4】")
    return input("请选择您要办理的业务：")

while True:
    keyboard_input= main()
    if keyboard_input == "1":
        print(f"客户{name}当前银行卡余额为：{query()}")
        continue  # 通过continue继续下一次循环，一进来就是回到了主菜单
    elif keyboard_input == "2":
        add(int(input("请输入要存款的金额：")))
        continue  # 通过continue继续下一次循环，一进来就是回到了主菜单
    elif keyboard_input == "3":
        sub(int(input("请输入要取款的金额：")))
        continue  # 通过continue继续下一次循环，一进来就是回到了主菜单
    else:
        print("程序退出！！！")
        break



