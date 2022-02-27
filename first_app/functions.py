# reduce() function-------
# from functools import *
# lst = [1,2,3,4]
# result = reduce(lambda x,y:x+y,lst)
# print(result)

# map() function------------
# lst= [1,2,3,4]
# result = list(map(lambda x:x*3, lst))
# print(result)

# filter() function------

# lst = [1,2,3,4]
# result = list(filter(lambda x:x%2==0, lst))
# print(result)


# decorator
# def decor(func):        
#     def inner(numb):
#         if numb==2:
#             print("Number is two-",numb)
#         else:
#             func(numb)
#     return inner

# @decor
# def wish(numb):
#     print("the wish number-",numb)

# wish(2)
# wish(3)
# wish(4)




# oops

from itertools import product
from typing_extensions import Self


class Product:
    def __init__(self, name, price, qty):
        self.name = "Mobile"
        self.price = 10,000
        self.qty = 1

    def display(self):
        print(self.name)
        print(self.price)
        print(self.qty)

x = Product()
x.display()
print(x.name, x.price, x.qty)