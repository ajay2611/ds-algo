# def super_reduced_string(s):
#     i = 0
#     ls = list(s)
#     while(i+1 < len(ls)):
#         if ls[i] == ls[i+1]:
#             del ls[i]
#             del ls[i]
#             i = 0
#             if i != 0:
#                 i -= 1
#         else:
#             i += 1
    
#     if len(ls):
#         return ''.join(ls)
#     else:
#         return 'Empty String'


def super_reduced_string(s):
    res = []
    for c in s:
        if res and res[len(res)-1] == c:
            res.pop()
        else:
            res.append(c)

    res = ''.join(res)
    return res or 'Empty String'

s = input().strip()
result = super_reduced_string(s)
print(result)