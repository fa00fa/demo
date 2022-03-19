# import random
# def random_hz_str(length):
#     words=[chr(random.randint(20000,21000)) for i in range(length)]
#     print(''.join(words))
#
# random_hz_str(50)
# # print(ord('a'))
# import uuid
# a=uuid.uuid4()
# print(a)
# b=uuid.uuid4()
# print(b)
# a=0
# b=a+1
#
#
# a=a+4
#
# print(a)
# print(b)
import copy
# a=[1,2]
# # b=a.copy()
# b=[1,2]
# print(id(a),id(b))
# print(a is b )
# print(a == b)
# alist=[{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':40}]
# alist.sort(key=lambda x:x['age'])
# print(alist)

# def foo():
#     for i in range(1000):
#         yield i
#
# x=foo()
#
# for r in x:
# #     print(r)
import sys
import time
# e={1,2,3}
# b={1,3,5}
#
# o=e & b
# print(o)
#
# def bar(a,b):
#     return set(a)-set(b)
# a=[1,2,3]
# b=[2,3,4]
# print(bar(a, b))
# @timer
# def foo(x,y):
#     return x**y
#
# #
# # foo(2, 20)
# def run_n_time(n):
#     def timer(fun):
#         def inner(*args, **kwargs):
#             start = time.time()
#             for i in range(n):
#                 result = fun(*args, **kwargs)
#             end = time.time()
#             print(result)
#             print(f'执行这个函数{n}次花费{end - start}秒')
#             return result
#         return inner
#     return timer
#
# @run_n_time(1000000)

# import time
# time.s
# from multiprocessing import Process
# def foo(x,y):
#     print(x**y)
#     return x**y
#
# tasks=[Process(target=foo,args=(2,20)) for i in range()]
#
# for t in tasks:
#     t.daemon=True
#     t.start()
# for t in tasks:
#     t.join()

# d={{2:4}:2}
# print(d,type(d))

# def foo(x=[]):
#     for i in range(len(x) - 1):
#         if x[i] > x[i + 1]:
#             x[i], x[i + 1] = x[i + 1], x[i]
#     return x[len(x)-1]
#
#
# a = foo([1, 900, 100, 4, 900.4, 6])
# print(a)
# import datetime

#
# #
# def cal_days(d1, d2=None):
#     date1 = datetime.datetime.strptime(d1, '%Y年%m月%d日')
#     if d2 is None:
#         date2 = datetime.datetime.now().today()
#     else:
#         date2 = datetime.datetime.strptime(d2, '%Y年%m月%d日')
#     all_second = abs(date1.timestamp() - date2.timestamp())
#     n_days = int(all_second // 86400)
#     return f'{n_days}天'
# #
# #
# print(cal_days('2020年11月1日', '2020年11月10日'))
# # d='2020年11月1日'
# day1=datetime.datetime.now().today().timestamp()
# day2=datetime.datetime.strptime(d,'%Y年%m月%d日').timestamp()
# print(day2)
# all_seconds=abs(day1-day2)
# print(all_seconds)
# days=all_seconds//86400
# print(days)
# '购买小鸡x只，母鸡y只，公鸡就是100-（x+y）'
#
# # for x in range(101):
# #     for y in range(34):
# #         z = 100 - x - y
# #         if x/3+y*3+z*5==100 and x >= 0 and y >= 0 and z>=0:
# #             print(f'小鸡{x}只，母鸡{y}只，公鸡{z}')
#
# for x in range(21):
#     for y in range(34):
#         z = 100 - x - y
#         if 5*x+3*y+(1/3)*z==100:
#             print(f'公鸡{x}只，母鸡{y}只，小鸡{z}只')
#
#
# def feibo(n):
#     num1 = 2
#     num2 = 2
#     for i in range(n - 2):
#         num1, num2 = num2, num1 + num2
#         print(num2)
#
#
# # feibo(10)
#
# import time


# num1 = 2
# num2 = 2
# while True:
#     num1, num2 = num2, num1 + num2
#     print(num2)
#     time.sleep(1)

# def fei():
#     num1 = 1
#     num2 = 1
#     while True:
#         num1, num2 = num2, num1 + num2
#         yield num2
# a=fei()
# import hashlib
# from hashlib import md5,sha256
# import os
# # a=os.urandom(16).hex()
# # print(a)
#
# p='asd123'
# p=p.encode('utf8')
# print(p)
# b=md5(p).hexdigest()
# d=hashlib.sha1(p).hexdigest()
# e=hashlib.sha224(p).hexdigest()
# c=sha256(p).hexdigest()
# g=hashlib.sha384(p).hexdigest()
# f=hashlib.sha512(p).hexdigest()
# print(b,len(b))
# print(c,len(c))
# print(d,len(d))
# print(e,len(e))
# print(g,len(g))
# # print(f,len(f))
# data={'app_key':'asdafwerds','app_id':'234hjsd','phone':'12132132','msg':'hello','vcode':'213411'}
# sorted(data.items())
# print(data)
# # d=sorted(data.items())
# # c=[ f'{k}={v}' for k,v in d]
# # b='&'.join([ f'{k}={v}' for k,v in d])
# # print(d)
# # print(c)
# # print(b,type(b))
#
# [1,3,2,3,1]  ,'66'
# (1*6+(1-1)*5)+((3-1)*6+(3-1)*5)
#
# def foo(list):
#     x = 0
#     for
#     for i in range(len(list)):
#         x+=list[i]*6+(list[i]-1)*5
import random
from math import ceil


# k = [1, 2, 3, 4]
# # random.shuffle(k)
# # print(k)
#
# # #
# def rand(n):
#     k = [1, 2, 3, 4]
#     r = []
#     for i in range(ceil(n / len(k))):
#         random.shuffle(k)
#         if i==0:
#             for j in k:
#                 r.append(j)
#         elif k[0]==r[len(r)-1]:
#             k[0],k[1]=k[1],k[0]
#             for p in k :
#                 r.append(p)
#         else:
#             for l in k:
#                 r.append(l)
#
#     print(r[:10],len(r[:10]))
# rand(10)
# for i in range(10):
#     k=[1,2,3,4]
#     random.shuffle(k)
#     print(k)

# r=[]
# k=[1,2,3,4]
# for i in range(5):
#     random.shuffle(k)
#     for j in k :
#         r.append(j)
# print(r)

# a=[[1,2,4,3],[3,6,7,9],[0,3,2,1]]
# c=[(i[0],i[1],i[2],i[3]) for i in a]
# print(c)

# e=[(1, 2, 4, 3), (3, 6, 7, 9), (0, 3, 2, 1)]
# f=[ {j,q,r,t} for j,q,r,t, in e]
# print(f)

# '0到100以内所以的质数'
# a=[]
# for i in range(2,100):
#     count=0
#     for j in range (2,i):
#         if i%j==0:
#             count+=1
#     if count==0:
#         print(i)


# print(b)
#
# m=101
# n=200
# l=[]
# for i in range(m+1,n):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#     if count==0:
#         l.append(i)
#
# print(len(l))

# def foo(m, n):
#     l = []
#     for i in range(m, n + 1):
#         count = 0
#         for j in range(2, i):
#             if i % j == 0:
#                 count += 1
#         if count == 0:
#             l.append(i)
#     print(len(l))
#
# k=input('请输入：')
# c=k.split(',')
# m,n=int(c[0]),int(c[1])
# foo(m,n)

#
# def feibo(n):
#     n1,n2=1,1
#     for i in range(n-2):
#         n1,n2=n2,n1+n2
#     return n2
#
# a=[0]
# n=int(input('请输入数字：'))
# for i in range(1,n):
#     f=feibo(i)
#     a.append(f)
# print(a)


# def feibo(n):
#     n1, n2 = 1, 1
#     for i in range(n - 2):
#         n1, n2 = n2, n1 + n2
#     return n2
#
# n=int(input('请输入长度：'))
# a=[0]
# for j in range(1,n):
#     n1, n2 = 1, 1
#     for i in range(n - 2):
#         n1, n2 = n2, n1 + n2
#     # a.append(feibo(i))
#     a.append(n2)
# print(a)

# def feibo(n):
#     a=[0]
#     for j in range(1,n):
#         n1, n2 = 1, 1
#         for i in range(j-2):
#             n1,n2=n2,n1+n2
#         a.append(n2)
#     print(a)
# n=int(input('请输入长度：'))
# feibo(n)

# a=[0]
# for j in range(1,n):
#     a.append(feibo(j))
# print(a)
# for i in range(len(list)-1):
#     for j in range(i+1,len(list)):
#         if list[i]==list[j]:
#             print(list[i])
#             break

#
# list=[8,4,1,0,4,5,3,2,3]
# list.sort(reverse=True)
# for i in range(len(list)-1):
#     if list[i]==list[i+1]:
#         print(list[i])
# #         break
# a={True:12}
# print(a,type(a))
a=[1,2,5,6,8,9,21,42]
b=[5,7,8,9,12,34,54]
l=[]
for i in a:
    if i < b[i]:
        l.append(i)





print(a)
print(b)
print(l)