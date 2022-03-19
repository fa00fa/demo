# h=0.08
# j=0
# while True:
#     h*=2
#     j+=1
#     if h>=8848.13*1000:
#         break
# print(j)、

# a=1
# b=[]
# def func(a,b):
#     a+=1
#     b+=[1]
# #
# func(a,b)
# print(a)
# print(b)
# import copy
# [1,2,[99,2],666]
#
# [1,2,[99,2]]
#
# [1,2,[1,2]]
#
# list1=[1,2,[1,2]]
# list2=copy.copy(list1)
# list3=copy.deepcopy(list1)
# list1.append(666)
# list1[2][0]=999
# print(list1)
# print(list2)
# print(list3)

# dict1={}
# print(dict1,type(dict1))
# dict2={3:5}
# print(dict2,type(dict2))
# dict4={(1,2,3):'think'}
# print(dict4,type(dict4))
# dict4={[1,2,3]:'think'}
# print(dict4,type(dict4))
#
# v+=[1
# # from 单利模式 import s
# a=[1,2,3,4,5,6,7,8,9]
# b=[i for i in a if i%2!=0]
# print(b)
d1={'name':'tom','age':20,'gender':'male'}
d2={'score':90,'weight':70}
# print(d1.values())
d1.update(d2)
print(d1)