
#
# l=[1,2,[3,4,['434',]]]
# list1=[]
# list1.append(l)
# while len(list1)!=0:
#     list2=list1.pop()
#     for i in list2:
#         if type(i) is list:
#             list1.append(i)
#         else:
#             print(i)



def  reverse(x):
    cmp=lambda a,b:(a>b)-(a<b)
    s=cmp(x,0)
    recv=int(str(s*x)[::-1])
    return s*recv

print(reverse(520))