# for x in range(0,34):
#     for y in range(0,51):
#         if 3*x+2*y+(1/3*(100-x-y))==100:
#             print(x,y,100-x-y)
# msgs={'tom':{'name':'tom','gender':'male','chinese':90,'math':87},
#           'john':{'name':'john','gender':'male','chinese':88,'math':76},
#           'merry':{'name':'merry','gender':'female','chinese':56,'math':98}}
#
# l=[1,2,3,4,5]
# a=l[:4]
# print(a)
# s={'a':2,'b':8}
# s.setdefault('n',5)
# s.setdefault('u',100)
# print(s)
# import json
# def to_json(data):
#     result1=json.dumps(data,ensure_ascii=False,sort_keys=True)
#     result2=json.dumps(data,ensure_ascii=False,separators=(',',':'))
#     print(result1,type(result1))
#     print(result2,type(result2))
#
# a={'s':1,'w':3,'e':4,'t':2,'y':1}
# to_json(a)
# s='esfdsdawasss'
# c=set(s)
# r=[]
# for j in c:
#     t=s.count(f'{j}')
#     r.append(t)
# o=[]
# for i in s:
#     if s.count(f'{i}')==max(r):
#         o.append(i)
#         break
# c='many people would list sanfranciso'
# l=c.split(' ')
# o=l[::-1]
# k=''
# for i in o:
#     k+=i+' '
#
# print(k)
def get_min_gap(arr, num1, num2):
    min_gap = 2**32
    index1, index2 = -1,-1
    for i,j in enumerate(arr):
        if j == num1 :
            index1 = i
            if index2 >= 0:
                min_gap = min(min_gap, index1 - index2)
        if j == num2 :
            index2 = i
            if index1 >= 0:
                min_gap = min(min_gap, index2 - index1)
    print min_gap
    return min_gap

a=[2,3,5,6,7,3,2,5,8,5,7,5,8,3,3,1,6,4,3,2]
get_min_gap(a,3,6)

import sm


