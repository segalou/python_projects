# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 11:53:13 2016

@author: sega_
"""

'''
#Simple version of doSomething

import sys

class A:
    s1 = 0
    __age = 12
    
    def doSomething(self,s):
        print s

def main():
    a = A()
    a.doSomething("1111")
    print a.s1
    
if __name__ == "__main__":
    main()
'''
    


#中文注释   
#dosomething.py  
#每种语言都有类似的dosomething工程 至少我用过的c++ nodejs delphi objectivec我知道有


class A:
    s1 = 333 #公共属性
    __age = 0 #私有属性 __开头
    
    def __init__(self,age): #构造器 专有函数 __开头 __结尾
        self.__age = age
        return
    
    def __del__(self): #析够 专有函数 __开头 __结尾
        print "destroyed"
        return #函数体没内容则必须有return 否则可有可无
        
    #private
    def __doSomething(self,s): #私有成员函数 __开头 无__结尾
        print self.__age #类内部访问私有属性 外部不可访问
        return

    #public
    def doSomething(self,s): #公共成员函数
        self.__doSomething(s) #类内部访问私有成员函数 外部不可访问  
        print s
        
    
class AA(A):
    def doSomething(self,s):#公共成员函数 覆盖父类A的同名公共成员函数
        print "==="
        print s
        print "==="
    
def doSomething(v):
    vv = v+1
    return vv

def main():
    a = A(111) #对象a对类A实例化
    a.doSomething('222') #调用对象的公共成员函数
    print a.s1 #访问对象的公共属性
    del a
    #授权垃圾回收销毁对象 python会自己处理必要时刻销毁（对象没引用了）
    #但是你后面的代码已经不能访问对象a了 你如果不写 del a 
    #python会在程序执行完统一销毁
    #java垃圾回收一样不是c＋＋那种即时销毁 这个是android跑多了卡顿的重要原因之一

    aa = AA(111)
    aa.doSomething('222')
    del aa
    
    print doSomething(444) #函数调用函数 同时被调用函数有返回值

print '------------------------'

if __name__ == '__main__':
    main()