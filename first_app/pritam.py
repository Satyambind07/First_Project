# a = [10,20,30]
# b = [10,20,30]
# res = list(map(lambda x,y:x*y,a,b))
# print(res)
# for i in res:
#     print(i)

# from functools import reduce


# a = [45,65,69,39,50]
# res = reduce(lambda x,y:x+y,a)
# print(res)

from functools import reduce
empty_list=[]
for i in range(1,100): 
    # print(i) 
    empty_list.append(i) 
    # print(empty_list)
    d=reduce(lambda x,y:x+y,empty_list)
print(d)



