class DataClass(object):
    '''
        切片：根据下标来获取序列对象的(部分)任意数据
        常用字符方法：
            capitalize(),首字母变大写
            endswith()/startswith(),是否以x结束/开始
            find(),检测x是否在字符串中
            isalnum(),判断是否是字母和数字
            isalpha(),判断是否是字母
            isdigit(),判断是否是数字
            islower(),判断是否是小写
            join(),循环取出所有值用x去连接
            lower()/upper(),大小写转换
            swapcase(),大写变小写,小写变大写
            lstrip()/rstrip()/strip(),移除左右两侧空白
            split(),切割字符串
            title(),将每个单词的首字母变成大写
            replace(old,new,count=None),old被换字符串,new替换字符串,count换多少个(无count表示全部替换)
            count(),统计出现的次数
    '''
    def char_manipulation(self):
        txt = 'Helo Python!'
        print(txt.find('P')) # 查找目标在序列中的位置返回下标,没找到返回-1
        print(txt.index('a')) # 检测字符串中是否包含目标返回下标,不包含返回异常:ValueError: substring not found
    def char_slice(self):
        txt = 'Hello World!'
        print('输出完整数据:%s'%txt)
        print('取第2-第5之间的数据:%s'%txt[2:5]) # 左闭又开原则:start<=value<end范围
        print('取第2开始所有数据:%s'%txt[2:])
        print('取开始到第3个数据:%s'%txt[:3]) # txt[0:3],0可以省略
        print('倒序输出:%s'%txt[::-1]) # 不可以切片倒序,可以先倒序在切片
    '''
        list:使用[]表示列表,数据项可增删改查,内存地址不变,数据项之间用(,)隔开,支持索引、切片,数据项可以是任意数据类型
        tuple:使用()表示元组,与列表类似,不可变序列,(,)分割,任意数据类型,当元组内只有一个元素时也要加上(,)号例如(1,),不加逗号就不是元组类型
        dict:使用{}表示字典,由键值对组成,通常使用键来访问数据,和列表一样支持增删改查,不是序列类型没有下标不能用索引是一个无序的键值集合,是python内置的高级数据类型,键值对用(,)分割
            键必须是不可变类型(字符串,元组),值可以是任意类型,每个键必须是唯一的,重复键后者会覆盖前者
    '''
    def list(self):
        list_data = [1,2.22,'张三','abcd',True]
        print(type(list_data))
        print(len(list_data)) # len()获取序列的长度
        # 查找
        print('输出完整列表:%s'%list_data)
        print('第一个元素:%s'%list_data[0])
        print('第2项到第3项数据:%s'%list_data[1:3]) # 左闭右开原则
        print('第3项开始获取所有:%s'%list_data[3:])
        print('倒叙输出:%s'%list_data[::-1])
        print('%s'%list_data*3) # 多次输出(复制)
        # 增加
        list_data.append(['ffff','FFFF']) # 增加一个列表
        list_data.append('8888') # 增加一个数据项
        print(list_data)
        # 插入
        list_data.insert(1,'插队的') # 指定位置插入数据
        print(list_data)
        # 批量增加
        list_data.extend(list(range(10)))
        list_data.extend(['aaaa','AAAA'])
        print(list_data)
        # 修改
        list_data[0] = 'AAAA'
        print('将第一个数据修改为AAAA:%s'%list_data)
        # 删除(del关键字)
        del list_data[1]
        print('删除[插队的]:%s'%list_data)
        # 批量删除
        del list_data[:3]
        print('删除前三个数据:%s'%list_data)
        # 删除指定数据项
        list_data.remove('8888') # 如果有多个元素,只会删除找到的第一个元素
        print('删除8888:%s'%list_data)
        # 弹出指定下标的元素(pop方法)
        a = list_data.pop(1) # 默认弹出最后一项
        print(list_data)
        print('pop弹出的元素:%s'%a)
        # 查找元素的索引/下标
        print('查找aaaa在列表的下标:%s'%list_data.index('aaaa'))
        print('在列表下标10到13中查找aaaa的下标:%s'%list_data.index('aaaa',10,13)) # 左闭右开
    def tuple(self):
        tuple = ('abc',89,1.333,True,'张三',['a','b'],89,'aaaa',89) # 元组一旦创建不可修改,只能进行查询,切片
        print(type(tuple))
        print(tuple)
        # 遍历元组
        for i in tuple:
            print(i)
        # 下标
        print('下标:{}'.format(tuple[1]))
        # 切片
        print('切片:{}'.format(tuple[1:3]))
        print('反向切片:{}'.format(tuple[::-1]))
        print('隔1取1反向切片:{}'.format(tuple[::-2]))
        print('倒数正取:{}'.format(tuple[-2:-1]))
        # 元组本身不可修改,但元组内的列表数据项可以进行修改
        tuple[5][0] = 'aaaa'
        print(tuple)
        # 统计元素出现的次数
        print(tuple.count(89))
    def dict(self):
        dict = {'pro':'刑法','shcool':'法外狂徒'}
        print(type(dict))
        print(len(dict))
        # 增加
        dict['name'] = '张三'
        dict['age'] = 30
        dict['pos'] = '法外狂徒'
        dict.update({'height':1.78})
        print(dict)
        # 查找
        print(dict.keys())  # 获取所有键
        print(dict.values())  # 获取所有值
        print(dict.items())  # 获取所有键和值
        print('名字:{}'.format(dict['name']))
        # 修改
        dict['name'] = '李四'
        dict.update({'age': 50})
        print(dict)
        # 删除
        del dict['shcool']
        print(dict)
        # 弹出
        a = dict.pop('pos')
        print(dict)
        print(a)
        # 排序
        print(sorted(dict.items(),key=lambda d:d[0])) # 按照ASCII码排序键
        # print(sorted(dict.items(), key=lambda d:d[1])) # 值排序,由于类型不一致无法排序
    def common_method(self):
        # + * in
        # +
        txt = 'Hello'
        txa = 'World'
        print(txt + txa)
        la = list(range(10))
        lb = list(range(11,20))
        print(la + lb)
        da = {'name':'张三'}
        # *
        print(txt*3)
        print(la*3)
        # in
        print('l' in txt)
        print('a' in txt)
        print(2 in la)
        print('name' in da)
dc = DataClass()
# dc.char_manipulation()
# dc.char_slice()
# dc.list()
# dc.tuple()
# dc.dict()
dc.common_method()