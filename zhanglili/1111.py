#求56~89步长为2的和
x=0
for i in range(56,90,2):
    x=x+i
print(x)

# 未知数求积得方法

# #九九乘法表
# for i in range (1,10):
#     for y in range (1,i+1):
#         print (y,'x',i,'=',y*i,end='\t')
#     print()

#冒泡
# l=[89,100,101,23,76,11,12,16]
# a=len(l)
# print(a)
# for i in range(a-1,0,-1):
#
#     for j in range(i):
#
#         if (l[j]>l[j+1]):
#             l[j],l[j+1]=l[j+1],l[j]
#
# print(l)


#继承
class Parent ():

    money = 10000000
    house = 100
    __yi_wu = '裤子'

    def shou_yi(self):
        print('点石成金')

p=parent(123)

class Child(Parent):
    ai_hao = '花钱'
    pass

c=Child()
print(c.ai_hao)
print(c.money )
print(c.shou_yi())




