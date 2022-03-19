# import time
# def Cal_time(fn):
#     def do_action():
#         start=time.time()
#         y=fn()
#         end=time.time()
#         print(f'花费了{end-start}秒')
#         return y
#     return do_action
#
# @Cal_time
# def Mutli():
#     x=1
#     for i in range(1,9910000):
#         x+=i
#     return x
#
#
# print(Mutli())
# a,b={'name':'tom','age':20}
# print(a,b)
# print('大家好我叫%%,我今年%d岁了'%(18))
# l=[3,2,4,5,6,7]
# import django