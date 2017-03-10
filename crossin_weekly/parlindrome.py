# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:30:39 2017

@author: sega.lou
"""
"""
def palindrome(n):
    result = []
    for i in range(1,10):
        for j in range(0,10):
            for k in range(0,10):
                if (i+j+k)*2 == n:
                    number = int(str(i)+str(j)+str(k)+str(k)+str(j)+str(i))
                    result.append(number)
                elif (i+j)*2+k == n:
                    number = int(str(i)+str(j)+str(k)+str(j)+str(i))
                    result.append(number)

    for number in result:
        print number

n = 52
palindrome(n)
"""

def parlindrome(n):
    result = []
    for i in range(10000,1000000):
        i_sum=0
        i_str = str(i)
        if i_str == i_str[::-1]:
            for j in i_str:
                i_sum+=int(j)
            if i_sum==n:
                result.append(i)
    for number in result:
        print number       
            
parlindrome(52)