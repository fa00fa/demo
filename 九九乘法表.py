# j=0
# while j<9:
#     j+=1
#     i=0
#     while i<j:
#         i+=1
#         print(i,'*',j,'=',(i*j),sep='',end='\t')
#     print()

# for j in range(1,7):
#     for i in range(1,j+1):
#         print(i, '*', j, '=', (i * j), sep='', end='\t')
#     print()
# sum = 0
# for i in range(100, 1001):
#     sum += i
# print(sum)
# 定义一个函数求偶数的累加和，参数是范围，如参数是n，则表示求1-n的范围内偶数的累加和，结果以返回值形式返出
# def get_double(n):
#     x = 0
#     for i in range(0, n + 1, 2):
#         if i % 2 == 0:
#             x += i
#     return x


# print(get_double(6))
# alist=[{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
#
# alist.sort(key=lambda x:x.get('age'),reverse=True)
# print(alist)

# def a():
#     return [lambda x: i * x for i in range(4)]
# print([m(3) for m in a()])
# b=[lambda x: i * x for i in range(4)]
# # print(b)
# n=set([1,1,2,3,3,3,4])
# print(n)
# print (r"\nwoow")
for i in range(1,10):
    for j in range(i,10):
        print(i, '*', j, '=', (i * j), sep='', end='\t')
    print()