class Main(object):
    '''
        流程控制：
            选择流程/分支流程
                单分支：if
                双分支：if-else
                多分支：if-elif-elif-...-else
            循环流程
                for
                while
    '''
    def If(self):
        # 选择流程-单分支
        age = 61
        if age >= 60:
            print('你可以退休了.')
        print('--end--')
    def If_else(self):
        # 选择流程-双分支
        age = 59
        if age >= 60:
            print('你可以退休了.')
        else:
            print('年龄不满足退休条件.')
    def If_elif_else(self):
        # 选择流程-多分支
        score = int(input('输入分数:'))
        if score >= 60 and score < 80:
            print('及格.')
        elif score >= 80 and score < 90:
            print('良好.')
        elif score >= 90:
            print('优秀')
        else:
            print('小于60不予评价.')
    def mora(self):
        # 选择流程-猜拳小游戏:0:石头 1:剪刀 2:布
        import random as rd # 随机数种子
        computer = rd.randint(0,2)
        user = int(input('出拳[0:石头-1:剪刀-2:布]:'))
        if user == 0 and computer == 1:
            print('你赢了')
        elif user == 1 and computer == 2:
            print('你赢了')
        elif user == 2 and computer == 0:
            print('你赢了')
        elif user == computer:
            print('平局')
        else:
            print('你输了')
    def If_nested(self):
        # 选择流程-嵌套
        score = int(input('分数:'))
        if score >= 60:
            credit = int(input('学分:'))
            if credit >= 1800 and score >= 80:
                print('给予称号[优秀毕业生]')
            elif credit >= 1200:
                print('给予称号[毕业生]')
            else:
                print('学分未满足条件.')
        else:
            print('成绩未满足条件.')
    def While(self):
        # 循环流程-while
        a = 1
        while a <= 100:
            print(a,end=' ')
            a+=1
    def While_mora(self):
        # 循环流程-猜拳
        mora = Main()
        a = 1
        while a <= 3:
            mora.mora()
            a+=1
    def While_9x9(self):
        # 循环流程-99乘法表
        y = 1
        while y <= 9:
            x = 1
            while x <= y:
                print('{}x{}={}'.format(x, y, x * y), end=' ')
                x += 1
            print()
            y += 1
    def While_right_triangle(self):
        # 循环流程-直角三角形反
        y = 7
        while y >= 1:
            x = 1
            while x <= y:
                print('*',end=' ')
                x+=1
            print()
            y-=1
    def While_isosceles_triangle(self):
        # 循环流程-等腰三角形
        y = 1
        h = 5
        while y <= h:
            xk = 1
            while xk <= h - y:
                print('-',end='')
                xk+=1
            x = 1
            while x <= y * 2 - 1:
                print('*',end='')
                x+=1
            print()
            y+=1
    def For(self):
        # 循环流程-for
        txt = 'Python'
        for i in txt:
            print(i)
    def For_range(self):
        # range()函数,一个数据集合列表
        # range(起始值,结束值,步长),左闭右开,步长不能为0
        # 打印1-100的累加和
        sum = 0
        for i in range(1,101):
            sum+=i
        print('sum=%d'%sum)
    def For_even(self):
        # 取50到200之间的偶数
        for i in range(50,201):
            if i % 2 == 0:
                print('偶数:%d'%i,end=' ')
            else:
                print('奇数:%d'%i)
    def For_9x9(self):
        # for嵌套
        for y in range(1,10):
            for x in range(1,y+1):
                print('%dx%d=%d'%(x,y,x*y),end=' ')
            print()

    # break和continue的使用
    # break:结束本层循环
    # continue:跳过本次循环
    # 此处采用for循环来演示这两个关键字,while同理不在演示
    def For_break(self):
        # 累加和大于100结束循环
        sum = 0
        for i in range(1,51):
            if sum > 100:
                print('到%d退出循环'%i)
                break
            sum+=i
    def For_continue(self):
        # 使用continue跳过偶数
        for i in range(1,51):
            if i % 2 == 0:
                continue
            print('奇数:%d'%i)
    def For_str_break(self):
        # 如果找到e终止循环
        for i in 'I Love Python':
            if i == 'e':
                break
            print(i,end=' ')
    def For_str_continue(self):
        # 不输出o
        for i in 'I Love Python':
            if i == 'o':
                continue
            print(i,end=' ')

    # for-else,提示作用(查找事件,登录事件等等..)
    # while-else,提示作用(查找事件,登录事件等等..),与for类似不做演示
    def For_else(self):
        # for i in range(10):
        #     if i >= 5:
        #         break
        # else:
        #     # 如果上面循环中break执行,此处将也不在执行
        #     print('执行完了.')
        u = 'admin'
        p = '123456'
        for i in range(3):
            user = input('账号:')
            pasw = input('密码:')
            if user == u and pasw == p:
                print('登录成功.')
                break
            else:
                print('输入错误(%d)'%(i+1))
        else:
            print('输入错误次数过多账号已锁定.')

    # 案例
    # 猜年龄
    def guess_age(self):
        import random as rd
        min = rd.randint(1,6)
        max = rd.randint(6,11)
        computer = rd.randint(min,max)
        for i in range(3):
            user = int(input('小明今年(%d-%d岁)猜猜具体多少岁:'%(min,max)))
            if user > computer:
                print('猜大了,在想想.')
            elif user < computer:
                print('猜小了,在想想.')
            else:
                print('猜对了,恭喜你.')
                break
        else:
            print('小明今年%d岁啊.'%computer)
            print('机会用完了,祝你下次成功.')
    # BMI计算
    def bmi(self):
        height = 1.78
        weight = 123.88
        count = weight / (height**2)
        if count < 18.5:
            print('BMI值:%.2f,过轻'%count)
        elif count >= 18.5 and count < 25:
            print('BMI值:%.2f,正常'%count)
        elif count >= 25 and count < 28:
            print('BMI值:%.2f,过重'%count)
        elif count >= 28 and count <= 32:
            print('BMI值:%.2f,肥胖'%count)
        elif count > 32:
            print('BMI值:%.2f,严重肥胖'%count)
a = Main()
# a.If()
# a.If_else()
# a.If_elif_else()
# a.mora()
# a.If_nested()
# a.While()
# a.While_mora()
# a.While_9x9()
# a.While_right_triangle()
# a.While_isosceles_triangle()
# a.For()
# a.For_range()
# a.For_even()
# a.For_9x9()
# a.For_break()
# a.For_continue()
# a.For_str_break()
# a.For_str_continue()
# a.For_else()
# a.guess_age()
# a.bmi()