a = [6, 5, 2, 4, 7, 8, 1, 3, 9]
# j=0
# while j<len(a) -1:
#     j+=1
#     i = 0
#     while i < len(a) - 1:
#         if a[i] > a[i + 1]:
#             a[i], a[i + 1] = a[i + 1], a[i]
#         i += 1
# print(a)
b=sorted(a)
print(b)