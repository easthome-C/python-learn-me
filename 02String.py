"""
一、演示字符串三种定义方式
-单引号定义
-双引号定义
-三引号定义
"""

name= '黑马'
print(name,type(name))

name="heihei"
print(name,type(name))

name="""
我是
三引号
"""
print(name,type(name))

name ='''
woshisandan
'''
print(name,type(name))

print("====================================================")
#在字符串中包含双引号
name='"黑马"'
print(name,type(name))

name="'heima'"
print(name,type(name))

# 转义字符
name="\"黑马\""
print(name,type(name))

name = '\'heima\''
print(name,type(name))

"""
二、字符串拼接

"""
# 字面量拼接
print("a"+"b")
# 字符串字面量和字符串变量拼接
name="黑马"
address="aaa"
print("我"+name+"==>"+address)
tel=11111111
print("我"+name+"==>"+address+",数字:"+str(tel))

# 字符串格式化        %s %d %f 站位符
print("字符串格式化  =====================      %s 站位符")
class_num=10
avg_salary=5.2

mssage= "Psssadasa%s,阿萨达大厦%s"%(class_num,avg_salary)
print(mssage)

text= "来%s去sssa"%name
print(text,type(text))

print("字符串格式化  =====================      %d 站位符 整数%f 站位符 浮点数")
name="黑马"
stock_price=123456.11
set_year=2025

mssage= "%s,成立于%d,估价为%f"%(name,set_year,stock_price)
print(mssage)

"""
格式化字符串精度
m.n控制宽度和精度
m为宽度
.n为小数点进度
 
"""
a=11
b=11.345

print("数字11宽度限制为5，结果为：%5d" % a)
print("数字11宽度限制为1，结果为：%1d" % a)
print("数字11.345宽度限制为7,最小精度为2，结果为：%7.2f" % b)
print("数字11.345宽度不限制,最小精度为2，结果为：%.2f" % b)

"""
字符串格式化方式2
快速格式化
f"内容{变量}"
"""

name="sadada"
a=2006
b=2006.111
print(f"萨达{name},s谁打的{a},浮点{b}")

"""
对表达式格式化

"""

print("1*1的结果为：%d啊啊啊%s"%((1*1),"haha"))
print(f"1*1的结果为：{1*1}")
print("字符串在python中的类型名为: %s"%type("aaa"))




