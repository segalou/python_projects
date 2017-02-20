# -*- coding: utf-8 -*-
"""
Created on Tue Nov 08 16:52:34 2016

@author: sega.lou
"""

'''
 1. Use a list as a stack #像栈一样使用列表
'''
 
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print stack
stack.pop() #删除最后一个对象
print stack
stack.pop()
print stack
stack.pop()
print stack


'''
2. use a list as a queue: #像队列一样使用列表
'''
from collections import deque #这里需要使用模块deque 

print '============='
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print queue
queue.popleft()                 # The first to arrive now leaves
print queue #Eric left

queue.popleft()
print queue #John left

'''
3. three built-in functions： 三个重要的内建函数
filter(), map(), and reduce().
'''
print '============='
def f(x): return x % 3 == 0 or x % 5 == 0
#f函数为定义整数对象x,x性质为是3或5的倍数
print filter(f, range(2, 25))  #筛选

def cube(x): return x*x*x #这里是立方计算 还可以使用 x**3的方法
print map(cube, range(1, 11)) #对列表的每个对象进行立方计算

seq = range(8)   #定义一个列表
def add(x, y): return x+y  #自定义函数，有两个形参
print map(add, seq, seq) #使用map函数，后两个参数为函数add对应的操作数，如果列表长度不一致会出现错误

def add(x,y): return x+y
print reduce(add,range(1,11))

'''
4. List comprehensions
'''
print '============='
matrix = [                    #此处定义一个矩阵
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
print matrix
print [[row[i] for row in matrix] for i in range(4)]


'''
5. The del statement #删除列表指定数据
'''
print '============='
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0] #删除下标为0的元素
print a

del a[2:4] #从列表中删除下标为2，3的元素
print a

del a[:] #全部删除 效果同 del a
print a

'''
6. Sets: 集合
'''
print '============='
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)               # create a set without duplicates
print fruit
print 'orange' in fruit
print 'crabgrass' in fruit

'''
7. enumerate()：#遍历元素及下标
'''
print '============='
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i,v

'''
8.zip() #将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。
'''
print '============='
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]

print zip(a,b)
print zip(b,c)

'''
9.reversed():反转
'''
print '============='
for i in reversed(xrange(1,10,2)):
    print i


'''
10.sorted(): 排序
'''
print '============='
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print f
