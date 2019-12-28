#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def triangles():
    a = [1]
    while True:
        yield a
        b = a[:] 
        for i in range(1,len(b)): 
            b[i] = pre[i] + pre[i - 1] 
        b.append(1) 
        pre = b[:] 
        a = b[:]
	
if __name__=='__main__':
    n = 0
    results = []
    for t in triangles():
        print(t)
        results.append(t)
        n = n + 1
        if n == 10:
            break
    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
        ]:
	    print('测试通过!')
    else:
        print('测试失败!')
	
	
	
# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
    front=[]
    behind=[]
    for ele in s:
        if ele!='.':
            front.append(ele)
        else:
            break
    for ele in s[-1::-1]:
        if ele!='.':
            behind.append(ele)
        else:
            behind.append(ele)
            break
    def fn1(x, y):
        return x * 10 + y
    def fn2(x, y):
        if y=='.':
            return x / 10
        else:
            return x / 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn1, map(char2num, front))+reduce(fn2, map(char2num, behind))
	
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
	
	
	
	
	
	
	
from functools import reduce
def is_palindrome(n):
    n_new=n
    factor=10
    num=[]
    while n_new//10!=0:
        num.append(n_new % 10)
        n_new=n_new//10
    num.append(n_new % 10)
    n_new = reduce(lambda x,y:x*10+y, num)
    if n_new==n:
        return True
    else:
        return False
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')	