a=10
b=10
a+=1
b+=a
print(type(a).__name__)
print(type(b).__name__)
print(type(b))
print(type("a+b"))

a = str(a)
str(b)
print(type(a),  type(b))

c=11.11
d=int(c)
print(
    type(c),c,
    type(d),d,
    type(float(a)),float(a)
)

# 运算符

# 算术运算符 + - * /  //取整  % 取余 **

print("9//2=",9//2)
print("9%2=",9%2)
print("2**3=",2**3)

# 赋值运算符 =

# 复合赋值运算符 +=  -=  *=  /=  %= **= //=
num = 1
print(num)
num += 1
print("num += 1:",num)
num -= 1
print("num -= 1:",num)
num *= 4
print("num *= 4:",num)
num /= 2
print("num /= 2:",num)


num=3
print("num=",num)
num %= 2
print("num %= 2:",num)
num **= 2
print("num **= 2:",num)

num=9
num //= 2
print("num //= 2:",num)



