# a=1,2,3,4
# print(a)
#
# a,b,c,d=[1,2,3,4]
# print(a)
# print(b)
# print(c)
# print(d)
#
# a={'age':'18','name':'张丽丽'}
# print(a['age'])
#
# x,y,z,*m=[1,2,3,4]
# print(x)
# print(y)
# print(z)
#
#
# a=1
# b=2
# c=a+b
# print(c)
#
# d=a*b
# print(d)
#
# print(b==d)
# print(b!=d)
# print(b==d and b==a)
# print(b==d or b==a)
#
# z=1234567
#
# print(z % 10)
#
# y=z//10
# print(y)
# print(y%10)
#
# x=y//10
# print(x)
# print(x%10)
#
# #成绩评定，0-60分不及格，60-70及格，71-80良好，81-100优秀
#
# b=[20,30,40,50,60,70,80,90,100]
# for a in b:
#     if(a>0 and a<60):
#         print('不及格')
#     elif(a>=60 and a<=70):
#         print('良好')
#     elif(a>=70 and a<=80):
#         print('良好')
#     elif(a>=80 and a>=100):
#         print('优秀')
#
#
#
# #求出10*9*8.。。。*1的阶乘
# x=1
# for i in range(10,0,-1):
#     x = x * i
# print(x)
#

#50以内猜出20这个数字
# a=20
# flag = True
# while flag:
#     b=int(input('请输入数字'))
#     if b>a:
#         print('大了')
#     elif b<a:
#         print('小了')
#     else:
#         print('答对了')
#         flag = False


# 找出299-345之间可以被4整除的数字
# for i in range(299,346):
#     if(i%4==0):
#         print(i)

# for i in range(299,346):
#     if(i%4!=0):
#         continue
#     print(i)


#定义一个求两个数商和余数的方法
# a=20
# b=30
# print(a%b)
# print(a//b)

# def shu (a,b):  #a,b 形参
#     print(a % b)
#     print(a // b)
# shu(20,30)  #方法调用

# def shu (a,b):
#     if(b==0):
#         return  None # return 返回值
#     else:
#         return (a%b, a//b)
# # res=shu(20,4) # 按照位置传参
# res=shu(a=10,b=20)
# if res is None:
#     print(res)
#     print('参数不能为空')
# else:
#     print(res)
#     print('余数为：',res[0],'商为：',res[1])


# 未知数求和的方法
# def sum1(name,*args,**kwargs): #*args接收动态位置参数，**kwargs接收动态关键字位置参数
#     print(name)
#     print(kwargs)
#     s=0
#     for i in args:
#         s=s + i
#     return s
# print(sum1(123456789))
# print(sum1(name= 'zhanglili'))


#面向对象
class cl:  #创建一个类

    res = None  #red为结果
    # def input(self,a,b):
    #     self.a=a
    #     self.b=b

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        self.res = self.a + self.b

    def div(self):
        self.res = self.a/self.b

    def get_result(self):
        print(self.res)


# c=cl()
#
# c.input(20,30)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()

# d = cl(10, 20)
# d.sum()
# d.get_result()

# #九九乘法表
# for i in range(1, 10):
#     for g in range(1, i+1):
#         print(g,'x',i,'=',g*i,end='\t' )
#
#     print()

#冒泡
# l=[1,5,2,9,6,30,10,15,89,100,14]
# lenght=len(l)
# for i in range (lenght-1,0,-1):
#     for h in range(i):
#         if (l[h]>l[h+1]):
#            l[h],l[h+1]=l[h+1],l[h]
# print(l)




# from zhanglili2 import day02
#
# print(day02.a)

from zhanglili2.day02 import  a
print(a)


# #  打开模式：r读取  w清空写入  a追加写入 b二进制模式，打开的文件没有可以用w创建
# a=open('ccc.txt','a') # open打开文件
# a.write('zhangliliwenjian你好\nyayayayay') # write 写入,\n换行
# print(a.writable()) #判断是否可以写入
# a.close()  # close 关闭
#
# a=open('ccc.txt','r')




# #字符串截取
# a='abcdefghijklmn'
# print(a[0]) #取第一位
# print(a[-1])#取倒数第一位
# print(a[1:-3])  #取第二位到倒数第三位
# print(a[::-1])  #倒序
# print(a[-1:0:-1])  #倒叙  倒数第一到第二
#
# l='abcd,cghf,lkhgt'
# print(l.sp)



# #格式化  format.
# for i in range(1,10):
#     for j in range(1,i+1):
#        print("{}x{}={}".format(j,i,j*i), end="\t")
#     print()


# #列表改单个数字，以及多个数字
# l=[1,2,3,4,5,6,78,]
# l[0]=12  # 改单个
# print(l)
# l[1:3]=18,30 #改多个
# print(l)

#列表新增数据
# l=[]   # 空值里面加入数据
# l.append("zhanglili")
# print(l)

l=[1,2,3,4] #按下标新增数据，后面的数据不变
# l.insert(1,'aiya')
# print(l)



#新增，修改
# d={"name":"小明","age":18,"sex":"男"}
# d.update({"addr":"上海闵行","学历":"本科"})
# print(d)





#异常分为 语法异常，和其他异常


# f = open('bbbbb.txt','r')    # 读取一个不存在的文件，此处为异常
# print(f.read())
# f.close()                    # 这时运行会报错

# 此时可以手动处理，处理方式如下：
# try:
#     f = open('bbbbb.txt', 'r')
#     print(f.read())
#     f.close()
# except:
#     print('文件不存在')
#
# print('操作完文件')


# def div(a, b):                    # 常识：除数不能为0，否则会报错
#     try:                          # 可以手动用try做处理
#         return a / b
#     except:                       # 若除数为0，返回空值
#         return
#
#
# print(div(10, 0))


# def div(a, b):  # 常识：除数不能为0，否则会报错
#     try:  # 可以手动用try做处理
#         return a / b
#     except ZeroDivisionError:  # 我们可以使用已知的异常名字来捕获特定的异常
#         return  # 前提是我们已经拿到异常的类型名字
#         # 这样做就可以避免捕捉其他异常而混乱
#
#
# print(div(10, 0))

#else和finally详见Wiki后台第七单元第九点

#自定义异常
# 用户自定义异常类型，只要该类继承了Exception类即可，至于类的主题内容用户自定义，可参考官方异常类
class CustomException(Exception):
    def __init__(self, value='值不能为0'):
        self.value = value

    def __str__(self):
        return self.value


a = 0                               # a==0时，触发异常；a==1时，不触发异常
try:
    if a == 0:
        print('a = {}触发异常'.format(a))
        raise CustomException
    print('a = {}未触发异常'.format(a))
except CustomException as e:
    print(e)




