'''
    输出
    格式化输出：%占位符，s字符串，d整数，f浮点数(.2f保留小数点前两位)
    \n换行符
'''
# name = '小明'
# age = 20
# print('我叫：%s，今年：%d岁'%(name,age))

# 输出练习
# name = '小明'
# tle = '1433223'
# addr = '火星北半球'
# print('='*20)
# 方法一
# print('姓名:%s'%name)
# print('手机号:%s'%tle)
# print('地址:%s'%addr)
# 方法二
# print('姓名：%s\n手机号：%s\n地址：%s'%(name,tle,addr))
# 方法三
# print('姓名:{}\n手机号:{}\n地址:{}'.format(name,tle,addr))
# print('='*20)

'''
    输入：输入的数据类型均为str类型
'''
# name = input('姓名:')
# tle = input('电话:')
# addr = input('地址:')
# print('='*20)
# print('姓名:{}\n手机号:{}\n地址:{}'.format(name,tle,addr))
# print('='*20)

# 输入练习
a = int(input('第一个数：'))
b = int(input('第二个数：'))
print('{}+{}={}'.format(a,b,a + b))