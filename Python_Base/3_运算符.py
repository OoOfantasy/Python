'''
    算数运算符：+ - * / **(指数,次方[a的b次方 a ** b]) %(取余) //(取商,忽略小数只保留整数,向下取整[负数时需注意])
'''
def maina():
    a,b = 7,3
    c = a + b
    print(c)
    c = a - b
    print(c)
    c = a * b
    print(c)
    c = a / b
    print(c)
    c = a ** b
    print(c)
    c = a % b
    print(c)
    c = a // b
    print(c)
# maina()

'''
    比较运算符：== != > < >= <=,结果是布尔值(True False)
'''
def mainb():
    a,b = 1,2
    print(a == b)
    print(a != b)
    print(a > b)
    print(a < b)
    print(a >= b)
    print(a <= b)
# mainb()

'''
    逻辑运算符：and or not
    优先级：() -> not -> and -> or
'''
def mainc():
    a,b,c,d = 20,10,5,1
    print(a + b > c and c < d) # 两边结果为True才为True，否则为False
    print(c > d and a > b)

    print(a > b or c < d) # 一边为True结果就为True，都为False结果为False

    print(not a > b) # 取反，真假切换，黑白颠倒

    print(2 > 1 and 1 < 4 or 2 < 3 and 9 > 6 or 2 < 4 and 3 < 2)
    # T and T = T,T and T = T,T and F = F
    # T or T or F
    # T or F
    # T
    # 所以结果为True
# mainc()

'''
    赋值运算符：= += -= *= /= %= **= //=,算数运算的扩展
'''
def maind():
    a,b = 2,10
    a += b
    print(a)
    a -= b
    print(a)
    a *= b
    print(a)
    a /= b
    print(a)
    a %= b
    print(a)
    a **= b
    print(a)
    a //= b
    print(a)
# maind()