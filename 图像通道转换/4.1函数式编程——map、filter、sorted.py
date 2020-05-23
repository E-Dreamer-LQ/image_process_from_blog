# -*- coding: utf-8 -*-
'''
map()函数接收两个参数，一个是函数，
一个是Iterable，map将传入的函数依次作用到序列的每个元素，
并把结果作为新的Iterator返回
'''
def f(x):
    return x*x
r = map(f,[1,2,3,4])
print("output1:",list(r))


## map 实现list所有数字转为字符串
print("output2:",list(map(str, [1, 2, 3, 4])))


### reduce的用法reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return x + y
print("output3:",reduce(add,[1, 3, 5, 7, 9]))

#reduce实现把序列[1, 3, 5, 7, 9]变换成整数13579
def alter(x,y):
    return x*10+y
print("output4",reduce(alter,[1, 3, 5, 7, 9]))

## map 和 reduce组合实现‘13579’->13579
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
output5 = reduce(alter, map(char2num, '13579'))
print("output5",output5)

'''
实现的字符串转数字
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
str2int('13579')
'''
'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
'''

def normalize(name):
    name=name.lower()
    name=name.capitalize()
    return name
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print("output6",L2)


'''
编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''
def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L) 
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}

def char2num(s):
    return DIGITS[s]
def char2float2(s):
    c=s.index('.')
    a= list(map(char2num, s))
    a.pop(c)
    return (reduce(lambda x,y : x*10 + y, a))/10**(len(a)-c)

print("ouput7:",char2float2('123.456'))





